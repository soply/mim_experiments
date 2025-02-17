# coding: utf8
"""
File to run real data experiments.
"""
import json
import os
import sys
import time

import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import GridSearchCV as GSCV
from sklearn.model_selection import KFold, ShuffleSplit

from utils import load_data_set, load_estimator
from settings import get_settings

# Relative path leading to the repositories "github.com/soply/db_hand",
# "github.com/soply/simple_estimation", "github.com/soply/nsim_algorithm",
# "github.com/dclambert/Python-ELM"
path_to_source = '../..'


def run_experiment(arguments):
    # Load data set
    X, Y, log_tf = load_data_set(arguments['dataset'], path_to_source)
    estim = load_estimator(arguments['estimator_kwargs'], path_to_source)
    # Prepare for experiments
    n_test_sets = arguments['n_test_sets']
    test_size = arguments['test_size']
    param_grid = arguments['param_grid'] # Parameter grid for estimator to CV over
    cv_folds = arguments['cv_folds']
    n_jobs = arguments['n_jobs']
    kf = ShuffleSplit(n_splits = arguments['n_test_sets'],
                        test_size = arguments['test_size'])
    test_error = np.zeros(n_test_sets)
    best_parameters = {}
    test_iter = 0
    computational_time = np.zeros(n_test_sets)
    # Extra array to store dot products if estimator is nsim
    for idx_train, idx_test in kf.split(X):
        start = time.time()
        reg = GSCV(estimator = estim, param_grid = param_grid,
                   scoring = 'neg_mean_squared_error', iid = False,
                   cv = cv_folds, verbose = 0,
                   pre_dispatch = n_jobs,
                   error_score = np.nan,
                   refit = True) # If estimator fitting raises an exception
        X_train, Y_train = X[idx_train,:], Y[idx_train]
        X_test, Y_test = X[idx_test,:], Y[idx_test]
        reg = reg.fit(X_train, Y_train)
        Y_predict = reg.best_estimator_.predict(X_test)
        end = time.time()
        best_parameters[test_iter] = reg.best_params_
        if log_tf:
            test_error[test_iter] = np.sqrt(mean_squared_error(np.exp(Y_test), np.exp(Y_predict)))
        else:
            test_error[test_iter] = np.sqrt(mean_squared_error(Y_test, Y_predict))
        computational_time[test_iter] = end - start
        test_iter += 1
        print best_parameters
        print test_error
    # Save results
    mean_error = np.mean(test_error)
    std_error = np.std(test_error)
    mean_computational_time = np.mean(computational_time)
    filename = arguments['filename_base'] + '/' + arguments['dataset'] + '/' + arguments['estimator_kwargs']['method']
    filename_mod = filename
    save_itr = 0
    while os.path.exists('../results/' + filename_mod + '/'):
        save_itr += 1
        filename_mod = filename + '_' + str(save_itr)
    else:
        os.makedirs('../results/' + filename_mod + '/')
        np.save('../results/' + filename_mod + '/test_errors.npy', test_error)
        np.savetxt('../results/' + filename_mod + '/test_errors.txt', test_error)
        np.savetxt('../results/' + filename_mod + '/computational_time.txt', computational_time)
        np.savetxt('../results/' + filename_mod + '/computational_time_summary.txt', [mean_computational_time])
        np.savetxt('../results/' + filename_mod + '/test_errors_summary.txt', np.array([mean_error, std_error]))
        np.save('../results/' + filename_mod + '/best_params.npy', best_parameters)
        with open('../results/' + filename_mod + '/best_params_json.txt', 'w') as file:
            file.write(json.dumps(best_parameters, indent=4))
        with open('../results/' + filename_mod + '/log.txt', 'w') as file:
            file.write(json.dumps(arguments, indent=4))
    import pdb 
    pdb.set_trace()




if __name__ == '__main__':
    # Get number of jobs from sys.argv
    if len(sys.argv) > 1:
        n_jobs = int(sys.argv[1])
    else:
        n_jobs = 1 # Default 1 jobs
    print 'Using n_jobs = {0}'.format(n_jobs)
    # Data set
    datasets = ['airquality', 'boston', 'concrete', 'ames', 'skillcraft', 'yacht']
    methods = ['SIR', 'SIRII', 'SAVE', 'DR', 'PHD', 'RCLR', 'PHD']
    for method in methods:
        for dataset in datasets:
            arguments = get_settings(dataset)
            arguments.update({
                'filename_base' : 'test_1', # Name to store results
                'n_jobs' : n_jobs, # number of jobs to run in cv mode
                'estimator_kwargs' : { # Estimator details, content depends on the estimator
                    "method" : method,
                    "split_by" : "dyadic",
                    "use_residuals" : False,
                    "whiten" : False,
                    "rescale" : False
                },
            })
            run_experiment(arguments)
