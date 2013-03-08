#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
test.wrong_input_output
"""

import unittest
from catdd import Interface, validate, exceptions

class BehemothI(Interface):
    def __init__(self, array, boolean, dictionary, number, string):
        validate.Array(array)
        validate.Boolean(boolean)
        validate.Dictionary(dictionary)
        validate.Number(number)
        validate.String(string)
        return(validate.String)
        
class Behemoth(BehemothI):
    def __init__(self, array, boolean, dictionary, number, string):
        return(101)
        

class Test(unittest.TestCase):
    def test_01_not_array(self):
        self.assertRaises(exceptions.MethodInputError, 
                          Behemoth, None, True, {}, 1, 's')

    def test_02_not_bool(self):
        self.assertRaises(exceptions.MethodInputError, 
                          Behemoth, [], None, {}, 1, 's')

    def test_03_not_dict(self):
        self.assertRaises(exceptions.MethodInputError, 
                          Behemoth, [], True, None, 1, 's')

    def test_04_not_number(self):
        self.assertRaises(exceptions.MethodInputError, 
                          Behemoth, [], True, {}, None, 's')

    def test_05_not_string(self):
        self.assertRaises(exceptions.MethodInputError, 
                          Behemoth, [], True, {}, 1, None)

    def test_06_return_not_string(self):
        self.assertRaises(exceptions.MethodReturnValueError, 
                          Behemoth, [], True, {}, 1, 's')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()