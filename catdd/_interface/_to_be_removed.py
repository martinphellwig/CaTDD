#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
catdd._interface.rest
"""

from inspect import isfunction, getargspec, getsourcelines
import types



INTERFACES = 'interfaces'
IMPLEMENTS = 'implements'
ATTRIBUTES = 'attributes'




_ERROR = """
Interface Error on Class:
> %s (%s)
Implementing Interface(s):
> %s (%s)
On the following reasons:
"""

_ERROR_LABELS = """
Reserved keyword '%s' detected in class '%s'
Module location:
> %s
At line number %s
"""

_ERROR_INHERITANCE = """
Class %s used as an interface but not inherited from Interface.
"""

_ERROR_DEFINITION = """
Class %s declared as Interface but inherits from non-interface %s.
"""

def _error_implement(name, implement, interface, interface_function):
    raise(ValueError('Function missing in implement'))

def _error_interface(name, implement, interface, implement_function):
    raise(ValueError('Function missing in interface'))

def _signature_differ(attribute_implement, attribute_interface):
    print(attribute_implement.__code__)
    print(getsourcelines(attribute_implement))
    print(attribute_interface.__code__)
    print(getsourcelines(attribute_interface))

    pass

def _check_argspec(attribute_implement, attribute_interface):
    if getargspec(attribute_implement) != \
                                        getargspec(attribute_interface):
        _signature_differ(attribute_implement, attribute_interface)

    return(True)



