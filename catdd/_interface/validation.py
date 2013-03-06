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

ERROR_INHERITANCE = "Interface not Inherited from Interface"
ERROR_DEFINITION = "Interface Class %s based on Implement Class %s"

import inspect

def parent_is_catdd_interface(ifd, mro):
    test = mro[-1] 
    if test != ifd['Interface']:
        raise(ValueError(ERROR_INHERITANCE))

def parent_is_implement(ifd, previous, current):
    if previous[0] == 'implement':
        text = ERROR_DEFINITION % (current[1], previous[1])
        raise(ValueError(text))
    
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
            missing.append([key, None])
        elif implement == None:
            missing.append([None, key])
        elif not method_signature_is_equal(interface, implement):
            unequal.append([interface, implement])

    if len(missing) > 0 or len(unequal) > 0:
        raise(ValueError(str(missing)+'\n'+str(unequal)))
