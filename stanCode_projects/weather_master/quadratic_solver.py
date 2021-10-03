"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print('stanCode Quadratic Solver! ')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	y = b*b - 4*a*c
	if y < 0:
		print('No real roots')
	elif y == 0:
		x2 = (-b + math.sqrt(y)) / (2 * a)
		print('One root: '+str(x2))
	elif y > 0:
		x1 = (-b + math.sqrt(y)) / (2 * a)
		x2 = (-b + math.sqrt(y)) / (2 * a)
		print('Two real roots: ' + str(x1) + ',' + str(x2))




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
