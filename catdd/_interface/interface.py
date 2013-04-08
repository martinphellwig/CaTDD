#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Module containing the Interface base classes.
"""
from .wrappers import create_new_object, ignore_validation
# The Interface Dictionary Template, that is copied and filled.
# It is used throughout the resolving and validation process.
IFD = {'validation_type':None, # How strict in comparing interface/implement
                               # This is actually set internally and reserved
                               # for future use.
       'new_class':None,  # The first argument that is of __new__
       'new_args':None,   # The list arguments that is of __new__
       'new_kwargs':None, # The keyword arguments of __new__
       'new_object':None, # The class of return_instance
       'Interface':None,  # The actual Interface class
       'user_interfaces':None, # The user defined Interfaces
       'user_implements':None, # The user defined Implements
       'user_attributes':None, # The user defined Attributes
       'return_instance':None} # The instance returned from new

class Interface(object):
    def __new__(cls, *args, **kwargs):
        ifd = IFD.copy()
        if ignore_validation(cls):
            ifd['validation_type'] = 'ignore'
        else:
            ifd['validation_type'] = 'strict'
            
        ifd['Interface'] = Interface
        ifd['new_class'] = cls
        ifd['new_args'] = args
        ifd['new_kwargs'] = kwargs
        ifd['new_object'] = create_new_object(ifd)
        ifd['return_instance'] = ifd['new_object']
        ifd['return_instance'] = ifd['new_object'](*args, **kwargs)
        return(ifd['return_instance'])

