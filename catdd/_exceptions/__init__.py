#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Exception Classes
"""
from .hook import ErrorCaTDD
from .exceptions import InterfaceError, InterfaceImplementError, \
                        InterfaceImplementInheritanceError, \
                        InterfaceImplementMethodError, MethodInputError, \
                        MethodReturnValueError, ValidationError

    