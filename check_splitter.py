"""
A program for splitting a check between multiple people.
"""

import math
import os

# Function Declarations
def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

def get_check_total():
    while True:
        try:
            total_of_check = float(input("What is the total of the check? $"))
            break
        except ValueError:
            clear_screen()
            print("\nPlease enter a valid check total.\n")

    return total_of_check

def get_num_of_people():
    while True:
        try:
            total_people = int(input("How many people? "))
            break
        except ValueError:
            clear_screen()
            print("\nPlease enter a valid number of people.\n")

    return total_people

def clear_screen():
    os.system('clear')

# Main Program Flow
clear_screen()
print("This program splits a check depending on the number of people.\n")

total_of_check = get_check_total()
total_persons = get_num_of_people()
cost_per_person = split_check(total_of_check, total_persons)

print(f"Total:    {total_of_check}\n# of Persons:   {total_persons}\nCost per person:   ${cost_per_person}")

