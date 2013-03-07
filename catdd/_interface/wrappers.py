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
import validation

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
        return(validation.method_execution(self.ifd, self.interface, 
                                           self.implement, args, kwargs))
    
def wrap_method(ifd, item):
    # Wrap the method so we have more control over it's actual runtime
    # execution, preserve as much as possible, i.e. func_* attributes.
    name = 'Wrapped method %s' % item['implement'].__name__
    type_dic = dict()
    for attribute in dir(item['implement']):
        if not (attribute.startswith('__') and attribute.endswith('__')):
            type_dic[attribute] = getattr(item['implement'], attribute)
            
    for attribute in ATTRIBUTES:
        type_dic[attribute] = getattr(item['implement'], attribute)
    
    if hasattr(item['interface'], '__doc__'):
        doc_string = item['interface'].__doc__
    else:
        doc_string = item['implement'].__doc__
    
    signature = introspection.get_signature(item['implement'])    
    doc = """>>> %s ... \n%s""" % (signature, doc_string)
    type_dic['__doc__'] = doc
    type_dic['func_archetype'] =  item['implement']
        
    WrapClass = type(name, (MethodWrapper,), type_dic)
    value = WrapClass(ifd, item['interface'], item['implement'])
    return(value)
    
    
def create_new_object(ifd):
    introspection.attributes(ifd) # Sets ifd['user_attributes'] 
    attributes = ifd['user_attributes']
    validation.interface_and_implement_are_equally_defined(ifd)
    
    type_dic = dict()
    for key in attributes:
        # If it is a class attribute map it direct.
        # Otherwise it is a method and wrap it.
        item = attributes[key]
        if 'attribute' in item:
            value = item['attribute']
        else:
            value = wrap_method(ifd, item)
        type_dic[key] = value
            
    class_object = type(ifd['new_class'].__name__, (object,), type_dic)
    return(class_object)
