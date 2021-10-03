"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    n = int(input('Enter a number: '))
    step = 0
    while n != 1:
        step += 1
        if n % 2 == 1:
            print( str(int(n)) + ' is odd, so I make 3n+1: ' + str(int(n*3+1)) )
            n = n*3+1
        else:
            print( str(int(n)) + ' is even, so I take half : ' + str(int(n/2)) )
            n = n/2
    print('It took ' + str(step) + ' steps to reach 1.')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
