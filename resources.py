import numpy as np
import pandas as pd

def import_movie_list():
    data = pd.read_csv('data\small_movie_list.csv', delimiter = ',' ,header = 0 , index_col =  0 )
    return data 

def import_movies_data(filelocation):
    data = np.loadtxt(filelocation , delimiter=',')
    return data

def mean_normalize_data2(Y,R):
    Y_mean = (np.sum(Y*R,axis=1)/np.sum(R,axis = 1)).reshape(-1,1)
    Y_norm = Y - np.multiply(Y_mean,R)
    return(Y_norm,Y_mean) 