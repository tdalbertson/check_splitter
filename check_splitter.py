"""
A program for splitting a check between multiple people.
"""

import math
import os

# Function Declarations
def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

def clear_screen():
    os.system('clear')

# Main Program Flow
clear_screen()
print("This program splits a check depending on the number of people.\n")

# Input Validation
while True:
    try:
        total_of_check = float(input("What is the total of the check? "))
        break
    except ValueError:
        clear_screen()
        print("\nPlease enter a valid check total.\n")
