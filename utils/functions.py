#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import io
import subprocess

from utils.log    import log
from utils.option import qlConfig

def readFile(filepath):
    if not os.path.isfile(filepath):
        return ""
    with open(filepath) as r:
        return r.read()

def dirFiles(dirpath):
    ret = []
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath):
            ret.append(filename)
    return ret


def execute(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')
    stream_stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8')
    str_stdout = stream_stdout.read()
    if qlConfig("debug").lower() == "on":
        str_stderr = stream_stderr.read()
        log.warning(str_stderr)
    
    return str_stdout


def cvsClean(content):
    return content.replace(",", " ").replace("\n", " ")