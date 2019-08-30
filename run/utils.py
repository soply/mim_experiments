# coding: utf8
"""
Contains utilities such as data set loader and estimator loader.
"""
import copy
import sys

import numpy as np


def load_data_set(dataset, path_to_source):
    """
    Loads a specific data set given by the identifier 'dataset'. Path to source
    should contain the data set handlers given in repository "github.com/soply/db_hand".

    Parameters
    ------------
    dataset : string
        Identifier for the data set

    path_to_source : string
        Folder where data set git repository "github.com/soply/db_hand" is cloned to.
    """
    sys.path.insert(0, path_to_source + '/DataSets/')
    log_tf = False
    if dataset == 'boston':
        from handler_UCI_Boston import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y) # Using Logarithmic Data
        log_tf = True
    elif dataset == 'auto_mpg':
        from handler_AutoMPG import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
    elif dataset == 'concrete':
        from handler_UCI_Concrete import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
    elif dataset == 'ames':
        from handler_AmesHousing import read_all
        data = read_all(scaling = 'MeanVar', feature_subset = 'intuitive')
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y) # Using Logarithmic Data
        log_tf = True
    elif dataset == 'istanbul':
        from handler_UCI_IstanbulStockExchange import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
    elif dataset == 'airquality':
        from handler_UCI_AirQuality import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
    elif dataset == 'powerplant':
        from handler_UCI_CombinedCyclePowerPlant import read_all
        data = read_all()
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y) # Using Logarithmic Data
        log_tf = True
    elif dataset == 'skillcraft':
        from handler_UCI_SkillCraft import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y) # Using Logarithmic Data
        log_tf = True
    elif dataset == 'airfoil':
        from handler_UCI_Airfoil import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
    elif dataset == 'yacht':
        from handler_UCI_Yacht import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y) # Using Logarithmic Data
        log_tf = True
    elif dataset == 'EUStockExchange':
        from handler_EUStockExchange import read_all
        data = read_all(scaling = 'MeanVar')
        X, Y = data[:,:-1], data[:,-1]
        Y = np.log(Y)
        log_tf = True
    else:
        raise NotImplementedError('Load data: Data set does not exist.')
    return X, Y, log_tf


def load_estimator(estimator_kwargs, path_to_source):
    """
    Parameters
    ------------
    estimator_kwargs : dict
        Contains estimator name, and additional arguments if necessary.

    path_to_source : string
        Folder where source code for other estimators is hosted.
    """
    # name = estimator_kwargs['estimator']
    # copy_dict = copy.deepcopy(estimator_kwargs)
    sys.path.insert(0, path_to_source + '/sdr_toolbox_dev/')
    from sdr_toolbox.sdrknn import SDRKnn
    return SDRKnn(n_neighbors = 1, n_components = 1, n_levelsets = 1, **estimator_kwargs)
