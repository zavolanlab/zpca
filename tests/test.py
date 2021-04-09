#!/usr/bin/env python

import os
import shutil
import hashlib
import pandas as pd

from zpca.zpca import counts2tpm, counts2tpm_many

TRANSCRIPT_COUNTS = "test_data/transcripts_counts.tsv"
TRANSCRIPT_LENGTHS = "test_data/transcripts_lengths.tsv"
TRANSCRIPT_TPM = "test_data/transcripts_tpm.tsv"
TRANSCRIPT_LENGTH = "test_data/transcripts_length.tsv"

TRANSCRIPT_TPM_2_SAMPLES = "test_data/transcripts_tpm_2_samples.tsv"
TRANSCRIPT_TPM_2_SAMPLES_PCA = "test_data/transcripts_tpm_2_samples_PCA.tsv"
TRANSCRIPT_TPM_2_SAMPLES_scree = "test_data/transcripts_tpm_2_samples_scree.tsv"

def test_counts2tpm():

    counts = pd.read_csv(
        TRANSCRIPT_COUNTS,
        header=0,
        sep="\t"
    )[["Name", "cond1_rep1"]]
    counts.set_index("Name", inplace=True)

    length = pd.read_csv(
        TRANSCRIPT_LENGTHS,
        header=0,
        sep="\t"
    )[["Name", "cond1_rep1"]]
    length.set_index("Name", inplace=True)
    length.columns = ["Length"]

    tpm = pd.read_csv(
        TRANSCRIPT_TPM,
        header=0,
        sep="\t"
    )[["Name", "cond1_rep1"]]
    tpm.set_index("Name", inplace=True)
    tpm.columns = ["original"]
    
    tpm_estimated = counts2tpm(counts, length)
    tpm_estimated.columns = ["estimated"]

    print(tpm_estimated.head())
    print(tpm.head())
    df = pd.merge(tpm, 
                  tpm_estimated, 
                  left_index=True, 
                  right_index=True)

    corr = df.corr(method="pearson").iloc[0,1]

    assert corr > 0.99

def test_counts2tpm_many():

    counts = pd.read_csv(
        TRANSCRIPT_COUNTS,
        header=0,
        sep="\t"
    )
    counts.set_index("Name", inplace=True)

    length = pd.read_csv(
        TRANSCRIPT_LENGTHS,
        header=0,
        sep="\t"
    )
    length.set_index("Name", inplace=True)

    tpm = pd.read_csv(
        TRANSCRIPT_TPM,
        header=0,
        sep="\t"
    )
    tpm.set_index("Name", inplace=True)

    tpm_estimated = counts2tpm_many(counts, length)

    corr = pd.DataFrame(tpm_estimated.corrwith(tpm, axis = 0))

    for i, row in corr.T.iteritems():
        assert row[0] > 0.99

def test_zpca_counts_path(script_runner):
    ret = script_runner.run('zpca-counts', '--help')
    assert ret.success
    
def test_zpca_tpm_path(script_runner):
    ret = script_runner.run('zpca-tpm', '--help')
    assert ret.success
    
def test_zpca_tpm_2_samples(script_runner):
    script_runner.run('zpca-tpm', 
                            '--tpm', 
                            TRANSCRIPT_TPM_2_SAMPLES, 
                            '--out', 
                            'test_data/TRANSCRIPT_TPM_2_SAMPLES', 
                            '--verbose')
    pca_out = pd.read_csv("test_data/TRANSCRIPT_TPM_2_SAMPLES/PCA.tsv", header=0, sep="\t")
    pca_control = pd.read_csv(TRANSCRIPT_TPM_2_SAMPLES_PCA, header=0, sep="\t")
    
    corr = pd.DataFrame(pca_out.corrwith(pca_control, axis = 0))

    for i, row in corr.T.iteritems():
        assert row[0] > 0.99
    
    scree_out = pd.read_csv("test_data/TRANSCRIPT_TPM_2_SAMPLES/scree.tsv", header=0, sep="\t", index_col=0)
    scree_control = pd.read_csv(TRANSCRIPT_TPM_2_SAMPLES_scree, header=0, sep="\t", index_col=0)
    
    assert scree_out.equals(scree_control)