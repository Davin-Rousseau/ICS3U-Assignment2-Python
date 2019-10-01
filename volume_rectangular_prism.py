#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This proogram calculates volume of a right rectangular prism
# with the user entering length, width, height in cm.


def main():
    # This function calculates volume
    print("We will be calculating the volume of a right rectangular prism. ")

    # input
    length = int(input("Enter length of prism (cm): "))
    width = int(input("Enter width of prism (cm): "))
    height = int(input("Enter height of prism (cm): "))

    # process
    volume = length * width * height

    # output
    print("")
    print("Volume is {}cm^3".format(volume))


if __name__ == "__main__":
    main()
