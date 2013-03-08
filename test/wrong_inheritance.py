#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 8 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
test.wrong_inheritance
"""

import unittest
from catdd import Interface, exceptions

class Base(Interface):
    pass

class PreImplement(Base):
    pass

class ReInterface(PreImplement, Interface):
    pass

class Implement(ReInterface):
    pass


class Test(unittest.TestCase):
    def test_wrong_inheritance(self):
        self.assertRaises(exceptions.InterfaceImplementInheritanceError, 
                          Implement)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()