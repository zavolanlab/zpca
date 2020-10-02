#!/usr/bin/env python

import os
import shutil
import hashlib

def test_zpca_path(script_runner):
    ret = script_runner.run('zpca', '--help')
    assert ret.success