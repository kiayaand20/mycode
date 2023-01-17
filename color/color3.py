#!/usr/bin/env python3
import crayons

""" 
This code is used to practice crayons and defining functions
"""

def main():
    """The main program"""
    print(crayons.cyan("Kiaya Anderson", bold=True)) # prints out my name in cyan and bold
    print(crayons.green("Learning Python is pretty cool!")) # prints out a sentence in green
    print(f'{crayons.yellow("yellow string")} white {crayons.black("black string")}') # prints out threestrings in three distinct colors


if __name__ == "__main__":
    main()
