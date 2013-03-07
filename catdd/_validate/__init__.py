#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Like readme1st.py but with validation.
"""
import inspect
from catdd._exceptions import ValidationError

class BaseValidation(object):
    def __init__(self, *args, **kwargs):
        self.validate(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        self.validate(*args, **kwargs)
        
    def validate(self, *args, **kwargs):
        pass
    
    def error(self, args, kwargs):
        frames = inspect.getouterframes(inspect.currentframe())
        frame = frames[3]
        raise(ValidationError(args[0], frame))

class String(BaseValidation):
    def validate(self, *args, **kwargs):
        test = args[0]
        if not isinstance(test, (str, unicode)):
            self.error(args, kwargs)
            
        

if __name__ == '__main__':
    String(1)
            