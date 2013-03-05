#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
catdd._interface.introspection
"""
from inspect import isfunction, getsource
import validation

def get_signature(function):
    source = getsource(function)
    tmp = list()
    for line in source.split('\n'):
        line = line.strip()
        line = line.split('#', 1)[0]
        tmp.append(line)
        
        test = line.replace(' ', '')
        if test.endswith('):'):
            break
    
    signature = ''.join(tmp)
    return(signature)

def resolve_inheritance(ifd):
    mro = list(ifd['new_class'].__mro__[:-1]) # -1 is always object
    validation.parent_is_catdd_interface(ifd, mro)
    mro = mro[:-1] # -1 is The catdd Interface class
    mro.reverse() # Oldest First
    # For each item see, if if it has a base from interface, 
    # if so it is an interface definition, otherwise it is an implement.
    definition = list() 
    for item in mro:
        defined = None
        if ifd['Interface'] in item.__bases__:
            defined = 'interface'
        else:
            defined = 'implement'
        
        definition.append([defined, item])
            
    previous = [None, None]
    interfaces = list()
    implements = list()
    
    for row in definition:
        defined_type = row[0]
        if defined_type == 'interface':
            validation.parent_is_implement(ifd, row, previous)
            interfaces.append(row[1])
        else:
            implements.append(row[1])
        previous = row
      
    ifd['user_interfaces'] = interfaces
    ifd['user_implements'] = implements
    return(True)  

def resolve_attributes(ifd): 
    # Each resolved attribute has a subdictionary with either 
    # interface and implement or attribute if it is not a function
    key_subjects = [['interface', ifd['user_interfaces']],
                    ['implement', ifd['user_implements']]]
    dic = dict() 
    
    for key, subjects in key_subjects:        
        for subject in subjects:
            for attribute_name in subject.__dict__:
                attribute_item = subject.__dict__[attribute_name]
                if isfunction(attribute_item):
                    if attribute_name not in dic:
                        dic[attribute_name] = {'interface':None,
                                               'implement':None}
                    dic[attribute_name][key] = attribute_item
                else:
                    set_attribute = False
                    if attribute_name not in dic:
                        set_attribute = True
                    elif attribute_item != None:
                        set_attribute = True
                    
                    if set_attribute:
                        sub = {'attribute':attribute_item}
                        dic[attribute_name] = sub
    
    ifd['user_attributes'] = dic 
    return(True)


def attributes(ifd):
    resolve_inheritance(ifd)
    resolve_attributes(ifd)
    return(True) 