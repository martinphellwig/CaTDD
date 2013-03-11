#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
"""
# Due to the nature of unit-test and coverage, this module will show up as
# not covered.
import sys
from introspection import get_codepoint

_BASE = """
Interface/Implement Error occurred
==================================
%s
""".strip()

_TRACE = """
Interfaces:
%s
------------------------------------------------------------------------------
%s
------------------------------------------------------------------------------
Implements:
%s
------------------------------------------------------------------------------
%s
------------------------------------------------------------------------------

Reason(s):
==========
%s
""".strip()


class _ExceptHook(object):
    def __init__(self, ifd):
        self.ifd = ifd
        
    def hook(self, *args):
        interfaces = list()
        for interface in self.ifd['user_interfaces']:
            interfaces.append('- %s' % interface.__name__)
        interfaces = '\n'.join(interfaces)

        implements = list()
        for implement in self.ifd['user_implements']:
            implements.append('- %s' % implement.__name__)
        implements = '\n'.join(implements)
        
        cp_implement = get_codepoint(self.ifd['user_implements'][-1])
        cp_interface = get_codepoint(self.ifd['user_interfaces'][-1])
        text = _TRACE % (interfaces, cp_interface, 
                         implements, cp_implement, args[1])
        text = _BASE % text
        self.write(text)
        
    def hook_plain(self, *args):
        text = _BASE % args[1] 
        self.write(text)
    
    def write(self, text):
        sys.stderr.write(text)
        sys.stderr.flush()


class ErrorCaTDD(ValueError):
    def __init__(self, ifd):
        self._ifd = ifd
        self.excepthook = _ExceptHook(ifd)
        self._string = ''

    def __str__(self):
        return(self._string)
