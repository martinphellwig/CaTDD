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
import sys
if sys.hexversion > 0x03000000:
    _STRING_TYPES = (str, )
else:
    _STRING_TYPES = (str, unicode)                                             #@UndefinedVariable

from .base import BaseValidation

class String(BaseValidation):
    def validate(self, *args, **kwargs):
        test = args[0]
        if not isinstance(test, (str, _STRING_TYPES)):
            self.error(args, kwargs)
                    
class Number(BaseValidation):
    def validate(self, *args, **kwargs):
        self.format = 'number'
        test = args[0]
        if not isinstance(test, (int, float)):
            self.error(args, kwargs)
        
class Boolean(BaseValidation):
    def validate(self, *args, **kwargs):
        self.format = 'boolean'
        test = args[0]
        if not isinstance(test, bool):
            self.error(args, kwargs)
        
class Dictionary(BaseValidation):
    def validate(self, *args, **kwargs):
        self.format = 'dictionary'
        test = args[0]
        if not isinstance(test, dict):
            self.error(args, kwargs)
        
class Array(BaseValidation):
    def validate(self, *args, **kwargs):
        self.format = 'array'            
        test = args[0]
        if not isinstance(test, (list, tuple, set)):
            self.error(args, kwargs)
