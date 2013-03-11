#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 11 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Multiple Inheritances of Interfaces and Implements are supported too as long
as you don't inherit from an implement and define that one as an interface.

There are ways how you can break this, however I struggle to find any use cases
that are actually reasonable and are not down to bad design. If you find one
please let me know.
"""

from catdd import Interface

class ExampleLeft(Interface):
    def left(self, text):
        pass
    
class ExampleRight(Interface):
    def right(self, text):
        pass
    
class ExampleLeftRight(ExampleLeft, ExampleRight, Interface):
    pass

class Example(ExampleLeftRight, Interface):
    def middle(self, text):
        pass
    
class ImplementedLeftRight(Example):
    def left(self, text):
        return('left')
    
    def right(self, text):
        return('right')

class Implement(ImplementedLeftRight):
    def middle(self, text):
        return('middle')
    
def main():
    implement = Implement()
    print(implement.left('')),
    print(implement.middle('')),
    print(implement.right(''))
    

if __name__ == '__main__':
    main()

