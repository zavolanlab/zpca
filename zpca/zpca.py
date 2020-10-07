import pandas as pd
from functools import reduce

def counts2tpm(counts_df, lengths_df):
    """Convert a table of raw counts to TPM
    Input-1: pandas dataframe of counts (the id should be the index)
    Input-2: pandas dataframe of lengths (the id should be the index)
    Output: pandas dataframe of TPMs
    """
    df = pd.merge(lengths_df, counts_df, left_index=True, right_index=True)
    counts = df.iloc[:,1:]
    rate = (counts).div(df.iloc[:,0], axis=0)
    denom = rate.sum()
    tpm = rate/denom*1e6
    return tpm

def counts2tpm_many(counts_df, lengths_df):
    """Convert a table of raw counts to TPM
    Input-1: pandas dataframe of counts (the id should be the index)
    Input-2: pandas dataframe of lengths (the id should be the index)
    Each sample has a different length column
    Output: pandas dataframe of TPMs
    """
    columns = counts_df.columns
    tpms = []
    for column in columns:
        temp_counts = pd.DataFrame(counts_df[column])
        temp_length = pd.DataFrame(lengths_df[column])
        temp_length.columns = ["Length"]
        tpms.append(counts2tpm(temp_counts, temp_length))
    tpm = reduce(lambda left,right: pd.merge(left, 
                                             right, 
                                             left_index=True, 
                                             right_index=True), tpms)
    return tpm