#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
"""
import inspect
import catdd

class BaseValidation(object):
    def __init__(self, *args, **kwargs):
        self.format = None
        self.validate(*args, **kwargs)
        
    def error(self, args, kwargs):
        frames = inspect.getouterframes(inspect.currentframe())
        frame = frames[3]
        raise(catdd.exceptions.ValidationError(args[0], frame, self))