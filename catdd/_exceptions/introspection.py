#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 7 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
catdd._exceptions.introspection
"""
from inspect import getsource, getfile, getsourcelines

_FILE = 'File "%s", line %s, in %s'

def get_codepoint(subject, end=False):
    source = getsourcelines(subject)
    file_line = source[-1]
    
    if end:
        code_name = source[0][-1]
        file_line += len(source[0]) - 1
    else:
        code_name = source[0][-1]
    
    file_name = getfile(subject)
    codepoint = _FILE % (file_name, file_line, code_name.strip())
    return(codepoint.strip())

def get_signature(function):
    source = getsource(function)
    tmp = list()
    for line in source.split('\n'):
        line = line.strip()
        line = line.split('#', 1)[0]
        tmp.append(line)
        
        test = line.replace(' ', '')
        if test.endswith('):'):
            break
    
    signature = ''.join(tmp)
    return(signature)

def get_parameter(frame):
    text = ''.join(frame[4]).strip()
    text = text.rsplit('(', 1)[1]
    text = text.rsplit(')', 1)[0]
    text = text.strip()
    return(text)

