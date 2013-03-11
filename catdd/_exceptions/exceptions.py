#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
catdd._exceptions.exception
"""
import sys
from .introspection import get_codepoint, get_signature, get_parameter
from .hook import ErrorCaTDD

_NOT_IN_INTERFACE = """
'%s' method in Implement not specified in Interface
%s
------------------------------------------------------------------------------
""".strip()

_NOT_IN_IMPLEMENT = """
'%s' method specified in Interface is not implemented
%s
------------------------------------------------------------------------------
""".strip()

_METHOD_NOT_EQUAL = """
'%s' method in Implement has different signature than specified in Interface
- interface: %s
- implement: %s
%s
%s
------------------------------------------------------------------------------
""".strip()

_NOT_INHERITED = """
Can not inherit from a non-interface '%s' class when specifying interface '%s'
%s
%s
""".strip()

_INPUT_INVALID = """
Invalid input argument for method '%s'
-------------------
Signature ....... : %s
Arguments ....... : %s
Keyword Arguments : %s
------------------- 
Parameter Name .. : %s
Expected Format . : %s
Actual Value .... : %s
Value type ...... : %s
-------------------
Code Pointer Method for Interface & Implement:
%s
%s
------------------------------------------------------------------------------
""".strip()

_RETURN_INVALID = """
Invalid return value for method '%s'
-------------------
Signature ....... : %s
Arguments ....... : %s
Keyword Arguments : %s
------------------- 
Expected Format . : %s
Return Value .... : %s
Return Type ..... : %s
-------------------
Code Pointer Method for Interface & Implement:
%s
%s
------------------------------------------------------------------------------
""".strip()


def _get_missing_error_text(ifd, interface, implement):
    if interface == None:
        name = implement
        codepoint = get_codepoint(ifd['user_attributes'][name]['implement'])
        text = _NOT_IN_INTERFACE
    elif implement == None:
        name = interface
        codepoint = get_codepoint(ifd['user_attributes'][name]['interface'])
        text = _NOT_IN_IMPLEMENT 
        
    return(text % (name, codepoint))

def _get_unequal_error_text(ifd, interface, implement):
    sig_interface = get_signature(interface)
    sig_implement = get_signature(implement)
    text = _METHOD_NOT_EQUAL % (implement.__name__, 
                                sig_interface, 
                                sig_implement, 
                                get_codepoint(interface),
                                get_codepoint(implement))
    return(text)
        




class InterfaceError(ErrorCaTDD):
    def __init__(self, ifd):
        ErrorCaTDD.__init__(self, ifd)
        sys.excepthook = self.excepthook.hook

class InterfaceImplementInheritanceError(ErrorCaTDD):
    def __init__(self, ifd, current, previous):
        ErrorCaTDD.__init__(self, ifd)
        sys.excepthook = self.excepthook.hook_plain
        name_current = current[1].__name__
        name_parent = previous[1].__name__
        cp_current = get_codepoint(current[1])
        cp_parent = get_codepoint(previous[1])
        self._string =  _NOT_INHERITED % (name_parent, name_current, 
                                          cp_parent, cp_current)


class InterfaceImplementError(InterfaceError):
    def __init__(self, ifd, missing, unequal):
        InterfaceError.__init__(self, ifd)
        tmp = list()
        for interface, implement in missing:
            tmp.append(_get_missing_error_text(ifd, interface, implement))
        
        for interface, implement in unequal:
            tmp.append(_get_unequal_error_text(ifd, interface, implement))
            
        self._string = '\n'.join(tmp)

class InterfaceImplementMethodError(InterfaceError):
    def __init__(self, ifd, interface, implement, args, kwargs, error):
        InterfaceError.__init__(self, ifd)
        
        
class MethodInputError(InterfaceImplementMethodError):
    def __init__(self, ifd, interface, implement, args, kwargs, error):
        InterfaceImplementMethodError.__init__(self, ifd, interface, implement, 
                                               args, kwargs, error)
        
        self._string = _INPUT_INVALID % (implement.__name__,
                                         get_signature(implement),
                                         args,
                                         kwargs,
                                         get_parameter(error.frame),
                                         error.format,
                                         str(error.argument),
                                         str(type(error.argument)),
                                         get_codepoint(interface),
                                         get_codepoint(implement))
              
                    
class MethodReturnValueError(InterfaceImplementMethodError):
    def __init__(self, ifd, interface, implement, args, kwargs, error):
        InterfaceImplementMethodError.__init__(self, ifd, interface, implement, 
                                               args, kwargs, error)

        self._string = _RETURN_INVALID % (implement.__name__,
                                          get_signature(implement),
                                          args,
                                          kwargs,
                                          error.format,
                                          str(error.argument),
                                          str(type(error.argument)),
                                          get_codepoint(interface, end=True),
                                          get_codepoint(implement, end=True))


class ValidationError(ErrorCaTDD):
    def __init__(self, argument, frame, validation):
        self.argument = argument
        self.frame = frame
        if validation.format == None: 
            self.format = validation.__class__.__name__
        else:
            self.format = validation.format