#!/usr/bin/env python3

# Created by: Austin-Harty
# Created on: Nov 2019
# This program calculates the temperature in
# fahenheit with the celsius as a given


def main():

    # input
    first_integer = int(input("Enter the first_integer: "))

    # process
    answer = (first_integer * 9/5) + 32

    # output
    print("")
    print("The answer is {0}  = {1}"
          .format(first_integer, answer))


if __name__ == "__main__":
    main()
