Contracts Assisted Test Driven Development - CaTDD
==================================================

Abstract
--------
This package provides functionality to integrate the basic principles
of 'Design by Contract'(TM)* with Test Driven Development for Python.
Essentially it is Interface Definitions with optional Type/Value 
validation to use in a pythonic way. 

Pythonic?
---------
A very valid objection towards Type/Value validation is that it is not
pythonic. Some of the arguments are; it encourages broken design, 
is bad for performance, increases bug count and makes code reuse harder.

These arguments are absolutely true and I agree with them without any 
reservation, this package has been created with that in mind.

Is it for me?
-------------
Most likely if you have to ask yourself that question, the answer is no.
This package is not aimed to add functionality to your project but to 
help with the communication between developers. 

This means you should avoid it if any of the following is true:
- You are small team shop, communication is not an issue.
- You make use of a framework, which does not requiring any modification
  (Something like Django for example)
- There are well established and working process streams 
  (i.e. Specifications, Documentation, howto's, rules)
- You are unconvinced of the benefits of Test Driven Development.

Which means that you might be interested if you are the opposite:
- A large/enterprise development group, communication is always an issue
- You are building a framework from scratch
- Your customers are your fellow developers, as such the code is the
  most accurate documentation (regardless whether other types are 
  available) 
- Test Driven Development is the only way to prevent total anarchy

How do I install it?
--------------------
In the above context, your project most likely already is packaged
in a certain way and you probably already have included external 
modules in your package to prevent different install version to break 
your application. So just copy the folder catdd into the folder where 
the other third party software components are and import from there.
Please do not put this package in site-packages.

How do I use it?
----------------
Let's assume your package 'xyz' folder is added to PYTHONPATH and
your third party software components folder 'tpsc' is added under that.

You will put the following line in the module where you define your 
interface:
>>> from xyz.tpc.catdd import Interface, validate
>>>
>>> class ExampleInterface(Interface):
...     def reverse(self, text):
...         validate.String(text)
...         return(validate.String)
>>>

And to use the above interface (i.e. the implement) you do: 
>>> class Example(ExampleInterface):
...     def reverse(self, text): 
...         return(text[::-1) 
>>>

That's it?
----------
Well, no, of course you should use docstrings in your Interface, see the 
readme1st.py in the examples folder, and perhaps split interface definitions 
and implements into different files.  

What actually happens?
----------------------
When you instantiate Example and call reverse method with a string, you will 
get returned a reversed string.

However, what actually happens is on instantiation the interface is
compared with the implement, requiring all functions in interface
to be present in the implement and the argument specification of the
functions to be the same. Then all the functions in the implement are 
wrapped, when you call a function the input parameters are first
called with ExampleInterface where we have defined some validation, the return
value of interface method is another validator. This validator is used with
the return value of the actual implement method. Finally if no exceptions
have been thrown, the return value of the implement method is returned.

If anything is incorrect you will get a modified stacktrace  explaining 
exactly what interface/implement went wrong and why it went wrong and, if 
appropriate, what input arguments where used.

What about the overhead?
------------------------
The overhead is considerably, this is the reason that when you create
a deploy version of your code, you replace the module catdd  with dummy, 
which also contains an Interface class and validate namespace but it is as the 
name suggest an empty one that does not do any of the above validation and 
checking.



------------------------------------------------------------------------
*) Design By Contract is a US registered trademark (78342277) by 
   Interactive Software Engineering, Inc. trading as Eiffel Software.