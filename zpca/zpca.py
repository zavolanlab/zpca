import pandas as pd

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