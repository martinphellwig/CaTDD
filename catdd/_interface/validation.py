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

INTERFACE = '__interface__'
ERROR_LABELS = "Reserved keyword '%s' used." % INTERFACE

def reserved_labels(subject):
    if INTERFACE in subject.__dict__:
        raise(ValueError(ERROR_LABELS))


