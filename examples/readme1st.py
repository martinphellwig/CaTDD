#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
This Module illustrates a simple and straight forward use of interface
without argument checking.
"""

from catdd import Interface

# This is the interface definition, note the elaborate docstring.
class StringOperationsI(Interface):
    """
    This is the docstring as defined in the interface.
    The implement will actually have this one too.
    """
    def reverse(self, text):
        """
        Reverses the input.
        
        Arguments:
         - Sequenced:
            - text (str, unicode); The text you would like to have 
                                   reversed.
              
         - Keyworded:
            - - - 
          
        Returns:
         - (str, unicode); The reverse of text
         
        Raises:
         - - -
         
        Example:
         >>> instance.reverse('abc')
         'cba'
         >>> 
         
        Notes:
         - - - 
        """
        pass


class StringOperations(StringOperationsI):
    def reverse(self, text):
        return(text[::-1])

# As you can see, when overriding the reverse method from the interface
# we can disperse of all the docstring as this will be still available by 
# means of wrapping, keeping the boilerplate to an absolute minimum while still
# have full use of the built-in documentation functionality.

def main():
    string_operations = StringOperations()
    input_string = 'abc'
    return_value = string_operations.reverse(input_string)
    print('output of reverse function >')
    print(return_value)
    print('<')
    print('Docstring of StringOperations Implement >')
    help(string_operations)
    print('<')
    print('Docstring of the reverse function of Implement >')
    help(string_operations.reverse)
    print('<')
    
if __name__ == '__main__':
    main()

