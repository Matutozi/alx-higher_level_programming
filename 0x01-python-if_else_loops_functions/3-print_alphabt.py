#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101 or letter == 113:
        letter += 1
    else:
        print("{:c}".format(letter), end="")
