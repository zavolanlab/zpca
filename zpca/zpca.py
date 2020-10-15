import pandas as pd
from functools import reduce
from sklearn.decomposition import PCA
from sklearn import preprocessing
import numpy as np
import random as rd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import sys

def determine_number_of_components(df):
    """Determine number of components based on the samples"""
    samples = list(df.shape)[1]
    if samples == 1:
        n_components = 1
        sys.stderr.write(f"Too few samples for PCA {os.linesep}")
        sys.exit(0)
    elif samples == 2:
        n_components = 2
    else:
        n_components = 3    
    return n_components

def perform_pca(df, n_components):
    """Run PCA analysis"""

    df = df.astype(float)

    scaled_data = preprocessing.scale(df.T, with_std=False)

    pca = PCA(n_components=n_components)
    pca.fit(scaled_data)
    pca_data = pca.transform(scaled_data)
    per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
    labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]

    return scaled_data, pca_data, per_var, labels

def generate_scree_plot(out, per_var, labels):
    """Generate scree plot"""
    plt.figure()
    plt.rcParams["figure.figsize"] = (20,20)
    plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)    
    plt.ylabel('Percentage of Explained Variance')
    plt.xlabel('Principal Component')
    plt.title('Scree Plot')
    plt.xticks(rotation='vertical')
    plt.savefig(os.path.join(out, "scree_plot.pdf"))
    plt.savefig(os.path.join(out, "scree_plot.png"))
    plt.close()
    
def generate_pc1_pc2_plot(out, pca_df, per_var):
    """Scatterplot PC1 and PC2"""
    plt.figure()
    plt.rcParams["figure.figsize"] = (20,20)
    plt.scatter(pca_df.PC1, pca_df.PC2)
    plt.xlabel('PC1 - {0}%'.format(per_var[0]), fontsize=22)
    plt.ylabel('PC2 - {0}%'.format(per_var[1]), fontsize=22)
    plt.title('PCA components 1 & 2', fontsize=22)
    for sample in pca_df.index:
        plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
    plt.savefig(os.path.join(out, "PCA_1_2.pdf"))
    plt.savefig(os.path.join(out, "PCA_1_2.png"))
    plt.close()
    
def generate_pc2_pc3_plot(out, pca_df, per_var):
    """Scatterplot PC1 and PC2"""
    plt.figure()
    plt.rcParams["figure.figsize"] = (20,20)
    plt.scatter(pca_df.PC2, pca_df.PC3)
    plt.xlabel('PC2 - {0}%'.format(per_var[1]), fontsize=22)
    plt.ylabel('PC3 - {0}%'.format(per_var[2]), fontsize=22)
    plt.title('PCA components 2 & 3', fontsize=22)
    for sample in pca_df.index:
        plt.annotate(sample, (pca_df.PC2.loc[sample], pca_df.PC3.loc[sample]))
    plt.savefig(os.path.join(out, "PCA_2_3.pdf"))
    plt.savefig(os.path.join(out, "PCA_2_3.png"))
    plt.close()

def generate_pc1_pc3_plot(out, pca_df, per_var):
    """Scatterplot PC1 and PC3"""
    plt.figure()
    plt.rcParams["figure.figsize"] = (20,20)
    plt.scatter(pca_df.PC1, pca_df.PC3)
    plt.xlabel('PC1 - {0}%'.format(per_var[0]), fontsize=22)
    plt.ylabel('PC3 - {0}%'.format(per_var[2]), fontsize=22)
    plt.title('PCA components 1 & 3', fontsize=22)
    for sample in pca_df.index:
        plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC3.loc[sample]))
    plt.savefig(os.path.join(out, "PCA_1_3.pdf"))
    plt.savefig(os.path.join(out, "PCA_1_3.png"))
    plt.close()

def generate_pca_3d(out, pca_df, per_var):
    """Scatterplot PC1, PC2, PC3"""
    labels = []
    pc1 = []
    pc2 = []
    pc3 = []
    for i, row in pca_df.iterrows():
        labels.append(i)
        pc1.append(row["PC1"])
        pc2.append(row["PC2"])
        pc3.append(row["PC3"])

    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(pc1, pc2, pc3)

    ax.set_xlabel('PC1 - {0}%'.format(per_var[0]))
    ax.set_ylabel('PC2 - {0}%'.format(per_var[1]))
    ax.set_zlabel('PC3 - {0}%'.format(per_var[2]))
    for label, x, y, z in zip(labels, pc1, pc2, pc3):
        ax.text(x, y, z, label)
    plt.savefig(os.path.join(out, "PCA_3D.pdf"))
    plt.savefig(os.path.join(out, "PCA_3D.png"))

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