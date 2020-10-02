import sys
import os
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def counts2tpm(counts_df, lengths_df):
    """Convert a table of raw counts to TPM
    Input-1: dataframe of counts (the id should be the index)
    Input-2: dataframe of lengths (the id should be the index)
    Output: dataframe of TPMs
    """
    df = pd.merge(lengths_df, counts_df, left_index=True, right_index=True)
    counts = df.iloc[:,1:]
    rate = (counts).div(df.iloc[:,0], axis=0)
    denom = rate.sum()
    tpm = rate/denom*1e6

    return tpm

