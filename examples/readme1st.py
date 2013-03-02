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
without argument checking. Please read the source from top to bottom as
it is described in detail. An explanation of the paradigm is given 
below.
"""

from catdd import Interface

# This is the interface definition, note the elaborate docstring.
class StringOperationsI(Interface):
    """This is the docstring as defined in the interface.
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


def main():
    string_operations = StringOperations()
    input_string = 'abc'
    return_value = string_operations.reverse(input_string)
    print('output of reverse function >')
    print(return_value)
    print('<')
    print('Docstring of StringOperations Implement >')
    print(help(string_operations))
    print('<')
    print('Docstring of the reverse function of Implement >')
    print(help(string_operations.reverse))
    print('<')
    
if __name__ == '__main__':
    main()

