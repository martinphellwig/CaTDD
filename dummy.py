#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Dummy Package, rename this to catdd when deploying your code, if you have a
deploy script capable of altering source on the fly, consider changing 
the inheritance from catdd.Interface to object.
"""

class Interface(object): pass

class _Validate(object):
    def __getattr__(self, name):
        subject_class = type(name, (_Validate,), dict())
        instance = subject_class()
        return(instance)
    
    def __call__(self, *args, **kwargs):
        return(args, kwargs)


validate = _Validate()