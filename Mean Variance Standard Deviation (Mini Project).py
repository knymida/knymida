#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        lst = np.array(list)
        new_list = lst.reshape((3,3))                   # reshaped list

        # sum of columns, rows and flattened array
        sum_r = np.sum(new_list, axis = 1).tolist()
        sum_c = np.sum(new_list, axis = 0).tolist()
        sum_f = np.sum(lst).tolist()


        # mean of columns, rows and flattened array

        mean_r = np.mean(new_list, axis=1).tolist()
        mean_c = np.mean(new_list, axis=0).tolist()
        mean_f = np.mean(lst).tolist()


        # variance of columns, rows and flattened array

        var_r = np.var(new_list, axis=1).tolist()
        var_c = np.var(new_list, axis=0).tolist()
        var_f = np.var(lst).tolist()


        # standard deviation of columns, rows and flattened array

        std_r = np.std(new_list, axis=1).tolist()
        std_c = np.std(new_list, axis=0).tolist()
        std_f = np.std(lst).tolist()


        # maximum of columns, rows and flattened array

        max_r = np.max(new_list, axis =1).tolist()
        max_c = np.max(new_list, axis =0).tolist()
        max_f = np.max(lst).tolist()


        # minimum of columns, rows and flattened array

        min_r = np.min(new_list, axis =1).tolist()
        min_c = np.min(new_list, axis =0).tolist()
        min_f = np.min(lst).tolist()


        calculations = {'mean': [mean_c, mean_r, mean_f],
                       'variance':[var_c, var_r, var_f],
                       'standard deviation': [std_c, std_r, std_f],
                       'max': [max_c, max_r, max_f],
                       'min': [min_c, min_r, min_f],
                       'sum': [sum_c, sum_r, sum_f]}
        return calculations

