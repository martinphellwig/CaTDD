#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
catdd._interface.validation
"""

import inspect
import catdd
    
def method_signature_is_equal(interface, implement):
    as_interface = inspect.getargspec(interface)
    as_implement = inspect.getargspec(implement)
    if as_interface == as_implement:
        return(True)
    else:
        return(False)
    
def interface_and_implement_are_equally_defined(ifd):
    missing = list()
    unequal = list()
    for key in ifd['user_attributes']:
        if 'attribute' in ifd['user_attributes'][key]:
            continue # Skip this specific iteration
        
        interface = ifd['user_attributes'][key]['interface']
        implement = ifd['user_attributes'][key]['implement']
        
        if interface == None:
            missing.append([None, key])
        elif implement == None:
            missing.append([key, None])
        elif not method_signature_is_equal(interface, implement):
            unequal.append([interface, implement])

    if len(missing) > 0 or len(unequal) > 0:
        raise(catdd.exceptions.InterfaceImplementError(ifd, missing, unequal))
    
def method_execution(ifd, interface, implement, args, kwargs):
    Error = catdd.exceptions.InterfaceImplementMethodError

    try:
        instance = ifd['return_instance']
        interface_return = interface(instance, *args, **kwargs)
    except catdd.exceptions.ValidationError as instance:
            raise(Error(ifd, interface, implement, 
                        args, kwargs, 
                        instance.frame, instance.argument))    
    
    implement_return = implement(instance, *args, **kwargs)
    
    #TODO: If an exception occurs here it means the return value is not 
    # according to specification
    if interface_return != None:
        try:
            interface_return(implement_return)
        except catdd.exceptions.ValidationError as instance:
            raise(Error(ifd, interface, implement, 
                        args, kwargs, instance.frame, instance.argument))    
        
    return(implement_return)
    