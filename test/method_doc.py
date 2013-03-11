#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 11 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
test.method_doc
"""

import unittest
from catdd import Interface

class ExampleI(Interface):
    def function(self):
        "function doc string"
        pass
    
class Implement(ExampleI):
    def function(self):
        "not this one"
        pass

class Test(unittest.TestCase):
    def testName(self):
        implement = Implement()
        expected = '>>> def function(self): ... \nfunction doc string'
        self.assertEqual(implement.function.__doc__, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()