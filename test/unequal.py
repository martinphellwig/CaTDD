#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
test.unequal
"""

import unittest
from catdd import Interface, exceptions

class UnequalSigI(Interface):
    def __init__(self, one):
        pass
    
class UnequalSig(UnequalSigI):
    def __init__(self, two):
        pass

class UnequalAttI(Interface):
    def one(self):
        pass
    
class UnequalAtt(UnequalAttI):
    def two(self):
        'DocString'
        pass

class Test(unittest.TestCase):
    def test_01_raises_unequal(self):
        self.assertRaises(exceptions.InterfaceImplementError, 
                          UnequalSig, '')
        
    def test_02_raises_unequal(self):
        self.assertRaises(exceptions.InterfaceImplementError, 
                          UnequalAtt, '')
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    