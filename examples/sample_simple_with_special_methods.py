#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Demonstrating that it's not a problem defining  special methods like the 
common __init__, __call__, __getattr__ and the more obscure __getattribute__.
Other attributes should work fine too, except for __new__.
Using __new__ in the context of interfaces does defeat the purpose of it as 
such it is not supported.
"""

from catdd import Interface, validate


class StringOperationsI(Interface):
    def __init__(self, text):
        validate.String(text)
        
    def __call__(self, one):
        validate.String(one)
        return(validate.String)

    def __getattr__(self, name):
        validate.String(name)
        
    def __getattribute__(self, name):
        validate.String(name)
        


class StringOperations(StringOperationsI):
    def __init__(self, text):
        self._name = text
        self._text = 'on_init_set "%s"' % text
        
    def __call__(self, one):
        return(self._text + '|' + one)
    
    def __getattr__(self, name):
        return('__getattr__:' + name)
        
    def __getattribute__(self, name):
        if name == '_name' or (name != self._name):
            return(object.__getattribute__(self, name))
        else:
            return('__getattribute__:'+self._text)
    

def main():
    string_operations = StringOperations('abc')
    print(string_operations('one'))
    print(string_operations.got_with_getattr)
    print(string_operations.abc)

if __name__ == '__main__':
    main()

