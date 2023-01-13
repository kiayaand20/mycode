#!/usr/bin/env python3

import crayons

def main():

    print(crayons.cyan("Kiaya Anderson", bold=True))
    print(crayons.green("Learning Python is pretty cool!"))
    print(f'{crayons.yellow("yellow string")} white {crayons.black("black string")}')


if __name__ == "__main__":
    main()
