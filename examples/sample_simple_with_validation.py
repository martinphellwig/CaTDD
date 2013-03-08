#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 5 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
Like readme1st.py but with validation.
"""

from catdd import Interface, validate


class StringOperationsI(Interface):
    def reverse(self, text):
        validate.String( text )
        return(validate.String)


class StringOperations(StringOperationsI):
    def reverse(self, text):
        return(text[::-1])

def main():
    string_operations = StringOperations()
    print(string_operations.reverse('abc'))

if __name__ == '__main__':
    main()

