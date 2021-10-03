"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
SENTINEL = -100


def main():
	print('stanCode "Weather Master 4.0"! ')
	day = 0
	total = 0
	cold = 0
	data = int(input('Next Temperature: (or -100 to quit)? '))
	if data == SENTINEL:
		print('No numbers were entered')
	else:
		maximum = data
		minimum = data
		while True:
			if data == SENTINEL:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if data < 16:
				cold = cold+1

			total = total+data
			day = day+1

			data = int(input('Next Temperature: (or -100 to quit)? '))

		print('Highest temperature= ' + str(maximum))
		print('lowest temperature= ' + str(minimum))
		print('Average= ' + str(total/day))
		print(str(cold) + ' cold day(s)')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
