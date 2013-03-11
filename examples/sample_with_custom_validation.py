#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 11 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
How to do custom validation.
"""

from catdd import Interface, validate

class DataValidation(validate.base.BaseValidation):
    # If format is not given, the class name is used
    format = """
    Compound Dictionary with the following structure:
    {'name':ASCIIString,
     'item':{'values':List}}"""

    # The method validate will be called with the argument given, note that
    # this will always be just on parameter.
    def validate(self, *args, **kwargs):       
        test = args[0]
        if not isinstance(test, dict):
            # If an error occurs, call self.error like this:
            self.error(args, kwargs)
             
            
        keys = ['name', 'item']
        for key in keys:
            if key not in test:
                self.error(args, kwargs)
                
        if 'values' not in test['item']:
            self.error(args, kwargs)
            
        if not isinstance(test['name'], (str)): # Python3 this will actually
                                                # also work for unicode
            self.error(args, kwargs)
            
        
        if not isinstance(test['item']['values'], (list, tuple)):
            self.error(args, kwargs)
    

class ExampleI(Interface):
    def __init__(self, data):
        DataValidation(data)
    
    
class Implements(ExampleI):
    def __init__(self, data):
        self.data = data

def main():
    data = {'name':'Myles',
            'items':{'values':['son']}}
    Implements(data)

if __name__ == '__main__':
    main()

