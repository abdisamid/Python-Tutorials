'''A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

Defining a Function
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
The first statement of a function can be an optional statement - the documentation string of the function or docstring.
The code block within every function starts with a colon (:) and is indented.
The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
Syntax
def functionname( parameters ): "function_docstring" function_suite return [expression] 
By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

Example
The following function takes a string as input parameter and prints it on standard screen.

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return'''
