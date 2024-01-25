#!/usr/bin/env python
"""
SYNOPSIS

    random_pass_gen.py
    No command line arguments involved.

DESCRIPTION

    Enter a number from 8 to 16,
    a randomised password will be output.

EXAMPLES

    User enters a number of 13.
    Output should givea randomised password, such as 'iuuqfAFWQF&2;'.

AUTHOR

    Dyn Candido <p276126@tafe.wa.edu.au>

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    1.0
"""
# Scenario 2 code
# Modules
import random

# Logic
# The character to randomly choose from.
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

# Welcome the user to the program.
print("Welcome to the random password generator.\n")

# Set pass_len to 0 to start WHILE loop.
pass_len = 0
# Continually ask user to enter the number until in the right range.
while pass_len < 8 or pass_len > 16:
    pass_len = int(input(
        "Please enter a number from 8 to 16 to generate your password: "))

# Set password to a blank string to later join values to it.
password = ""

# Loop through for as many times in the value of pass_len, adding a
# random character from char each time.
for i in range(pass_len):
    password += password.join(random.choice(char))

# Output final result.
print("Your generated password is:", password)
