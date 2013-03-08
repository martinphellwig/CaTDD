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
from catdd import Interface

class StringOperationsI(Interface):
    def reverse(self, text):
        pass
    
class StringOperation(StringOperationsI):
    def reverse(self, text):
        return(text[::-1])

    
class Test(unittest.TestCase):
    def test01_valid(self):
        test = StringOperation()
        expect = 'cba'
        self.assertEqual(test.reverse('abc'), expect)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()