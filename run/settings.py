# coding: utf8
import numpy as np


"""
File to get parameter settings for different data sets.
"""
def get_settings(dataset):
    if dataset == 'boston':
        arguments = {
            'dataset' : 'boston', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,60,3).tolist(),
                "n_levelsets": [2,4,6,8,10,12,14],
                "n_components" : [2,3,4,5,6,7,8],
            },
        }
    elif dataset == 'auto_mpg':
        arguments = {
            'dataset' : 'auto_mpg', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,60,3).tolist(),
                "n_levelsets": [2,3,4,5,6,7,8,10,12,14],
                "n_components" : [1,2,3,4],
            },
        }
    elif dataset == 'concrete':
        arguments = {
            'dataset' : 'concrete', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
                "n_levelsets": [2,4,6,8,10,12],
                "n_components" : [3,4,5,6,7,8],
            },
        }
    elif dataset == 'ames':
        arguments = {
            'dataset' : 'ames', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,60,3).tolist(),
                "n_levelsets": [2,4,6,8,10,12,14],
                "n_components" : [1,2,3,4,5,6,7],
            },
        }
    elif dataset == 'istanbul':
        arguments = {
            'dataset' : 'istanbul', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,60,3).tolist(),
                "n_levelsets": [2,4,6,8,10,12],
                "n_components" : [1,2,3,4,5,6,7],
            },
        }
    elif dataset == 'airquality':
        arguments = {
            'dataset' : 'airquality', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(10,150,5).tolist(),
                "n_levelsets": [2,4,6,8,10,12,14,16,18,20],
                "n_components" : [1,2,3,4,5,6,7,8,9,10,11],
            },
        }
    elif dataset == 'skillcraft':
        arguments = {
            'dataset' : 'skillcraft', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,40).tolist(),
                "n_levelsets": [1,2,3,4,5,6,7,8,9,10],
                "n_components" : [1,2,3,4,5,7],
            },
        }
    elif dataset == 'yacht':
        arguments = {
            'dataset' : 'yacht', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(1,20).tolist(),
                "n_levelsets": [1,2,3,4,5,6,7,8,9,10,11,12,13],
                "n_components" : [1,2,3,4,5,6],
            },
        }
    elif dataset == 'EUStockExchange':
        arguments = {
            'dataset' : 'EUStockExchange', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(5,92,3).tolist(),
                "n_levelsets": [1,2,3,4,5,6,7,8,9,10],
                "n_components" : [1,2,3],
            },
        }
    elif dataset == 'airfoil':
        arguments = {
            'dataset' : 'airfoil', # Data set identifier
            'n_test_sets' : 20, # number of repititions of the experiment
            'test_size' : 0.15, # size of the test set
            'cv_folds' : 5, # CV is used for parameter choices
            "param_grid": {
                "n_neighbors": np.arange(1,20).tolist(),
                "n_levelsets": [2,4,6,8,10,12,14,16],
                "n_components" : [1,2,3,4,5],
            },
        }
    return arguments
