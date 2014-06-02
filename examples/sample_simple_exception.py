#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 2 June 2014     
# All rights reserved.
# ============================================================================
#
"""
Example of what error we get when we don't implement the interface completely.
"""

from catdd import Interface, validate

class StringOperationsI(Interface):
    def reverse(self, text):
        return(validate.String)
    

class StringOperations(StringOperationsI):
    def reverse(self, text):
        return(1234)

def main():
    string_operations = StringOperations()
    print(string_operations.reverse('abc'))

if __name__ == '__main__':
    main()

