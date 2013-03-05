#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Basic Test
"""

import unittest
from catdd import Interface, validate
from catdd._exceptions import ExceptionCaTDD

class StringOperationsI(Interface):
    def reverse(self, text):
        validate.String(text)
        return(validate.String)

class StringOperationsIncompleteI(Interface): pass
    
class StringOperation(StringOperationsI):
    def reverse(self, text):
        return(text[::-1])

class StringOperationsIncompleteInterface(StringOperationsIncompleteI):
    def reverse(self, text):
        return(text[::-1])
    
class StringOperationsIncompleteImplement(StringOperationsI): pass
    
class Test(unittest.TestCase):
    def test01_valid(self):
        test = StringOperation()
        expect = 'cba'
        self.assertEqual(test.reverse('abc'), expect)

    def test02_not_defined_in_interface(self):
        self.assertRaises(ExceptionCaTDD, StringOperationsIncompleteInterface)

    def test03_not_defined_in_implement(self):
        self.assertRaises(ExceptionCaTDD, StringOperationsIncompleteImplement)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()