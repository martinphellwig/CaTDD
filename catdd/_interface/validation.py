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

from pprint import pprint

def parent_is_catdd_interface(ifd, mro):
    test = mro[-1] 
    if test != ifd['Interface']:
        raise(ValueError(ERROR_INHERITANCE))

def parent_is_implement(ifd, previous, current):
    if previous[0] == 'implement':
        text = ERROR_DEFINITION % (current[1], previous[1])
        raise(ValueError(text))
    
def interface_and_implement_are_equally_defined(ifd):
    missing = list()
    for key in ifd['user_attributes']:
        item = ifd['user_attributes'][key]
        if 'attribute' not in item:
            if item['interface'] == None:
                missing.append([key, None])
            elif item['implement'] == None:
                missing.append([None, key])
            else:
                # Both implement and interface are implemented
                pass
    
    if len(missing) > 0:
        raise(ValueError(str(missing)))
