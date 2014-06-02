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

class CustomValidation(validate.base.BaseValidation):                           #@UndefinedVariable
    # If format is not given, the class name is used
    format = """
    Compound Dictionary with the following structure:
    {'name':ASCIIString,
     'item':{'values':List}}"""

    # The method validate will be called with the argument given, note that
    # this will always be just one object, the one that is to be validated.
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
             
        if not isinstance(test['name'], (str)):
            self.error(args, kwargs)
             
        if not isinstance(test['item']['values'], (list, tuple)):
            self.error(args, kwargs)
    

class ExampleI(Interface):
    def who_is(self, data):
        CustomValidation(data)
        return(validate.String)
        
    
    
class Implements(ExampleI):
    def who_is(self, data):
        if data['item']['values'][0] == 'son':
            return_value = 'Who is your daddy?'
        else:
            return_value = 'Who is your mummy?'
        return(return_value)

def main():
    data = {'name':'Myles',
            'item':{'values':['son']}}
    implement = Implements()
    print(implement.who_is(data))
    

if __name__ == '__main__':
    main()

