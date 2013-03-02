#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ============================================================================
# Copyright (c) Martin P. Hellwig <martin.hellwig@gmail.com> 1 Mar 2013     
# All rights reserved.
# ============================================================================
#
"""
This class contains wrappers for methods and classes
"""
import introspection
ATTRIBUTES = ['__closure__', '__code__', '__hash__', '__repr__', '__str__']

class MethodWrapper(object):
    """
    Wraps the method of the interface class with optional validation
    against the same method of the implement.
    """
    def __init__(self, ifd, interface, implement):
        self.ifd = ifd
        self.interface = interface
        self.implement = implement
        
    def __call__(self, *args, **kwargs):
        instance = self.ifd['return_instance']
        interface_return = self.interface(instance, *args, **kwargs)
        implement_return = self.implement(instance, *args, **kwargs)
        if interface_return != None:
            interface_return(implement_return)
        
        return(implement_return)
    
def wrap_method(ifd, item):
    name = 'Wrapped method %s' % item['implement'].__name__
    type_dic = dict()
    for attribute in dir(item['implement']):
        if not (attribute.startswith('__') and attribute.endswith('__')):
            type_dic[attribute] = getattr(item['implement'], attribute)
            
    for attribute in ATTRIBUTES:
        type_dic[attribute] = getattr(item['implement'], attribute)
    
    signature = introspection.get_signature(item['implement'])
    doc = """>>> %s\n%s""" % (signature, item['implement'].__doc__)
    type_dic['__doc__'] = doc
    type_dic['func_archetype'] =  item['implement']
        
    WrapClass = type(name, (MethodWrapper,), type_dic)
    value = WrapClass(ifd, item['interface'], item['implement'])
    return(value)
    
    
def create_new_object(ifd):
    introspection.attributes(ifd) # Sets ifd['user_attributes'] 
    attributes = ifd['user_attributes']
    
    type_dic = dict()
    for key in attributes:
        # If it is a module attribute map it direct.
        # Otherwise it is a function and wrap it.
        item = attributes[key]
        if 'attribute' in item:
            value = item['attribute']
        else:
            value = wrap_method(ifd, item)
        type_dic[key] = value
            
    class_object = type(ifd['new_class'].__name__, (object,), type_dic)
    return(class_object)
