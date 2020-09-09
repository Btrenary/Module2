"""
Author: Brady Trenary
Program: camper_age_input.py

program that accepts and integer for years and returns an integer representing months

"""
import constants

def convert_to_months(years):
    months = years * constants.MONTHS
    return months

if __name__ == '__main__':
    age_in_years = input("Enter your childs age:")
    age_in_months = convert_to_months(int(age_in_years))
    print(f"{age_in_years} years is {age_in_months} months")