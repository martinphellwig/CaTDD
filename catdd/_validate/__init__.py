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
from catdd._exceptions import ValidationException

class String(object):
    def __init__(self, *args, **kwargs):
        self.validate(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        self.validate(*args, **kwargs)
    
    def validate(self, *args, **kwargs):
        test = args[0]
        if not isinstance(test, (str, unicode)):
            raise(ValidationException())
        

if __name__ == '__main__':
    String(1)
            