#!/usr/bin/env python

import os
import shutil
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def test_zpca_path(script_runner):
    ret = script_runner.run('zpca', '--help')
    assert ret.success

# def test_pca_loading_scores(script_runner):
#     tpm = "test_data/gene_expression.tsv"
#     loading_scores = "test_data/loading_scores.tsv"
#     out = "test_data/pca"
    

#     script_runner.run('zpca',
#                       '--tpm', tpm,
#                       '--out', out)

#     assert md5(loading_scores) == md5(os.path.join(out, "loading_scores.tsv"))

#     shutil.rmtree(out)