'''  
Module: Stellar Analytics 
"""
Module: utils_case

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Denise Case
This module provides a simple, reusable foundation for my analytics projects. 

TODO: Change the company name in this opening docstring
TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
'''
"""

#####################################
# Import Modules
#####################################

# Python Standard library imports
import statistics
# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add or replace this with your own boolean variable
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True

# declare an integer variable 
@@ -67,15 +75,39 @@
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

print("Starting........")
print(get_byline())
print("Complete.......")
@@ -84,7 +116,10 @@ def main() -> None:
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
main()

#TODO: Run this as a script to test that all functions work as intended.
#TODO: Run this as a script and verify all code works as intended.
