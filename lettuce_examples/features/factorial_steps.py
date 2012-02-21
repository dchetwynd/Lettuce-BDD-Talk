from lettuce import *

@step(r'I have an input of (\d+)')
def factorial_input(self, number):
	world.factorial_input = int(number)

@step(r'I calculate its factorial')
def calculate_factorial(step):
	world.result = factorial(world.factorial_input)

def factorial(number):
	if (number <= 1):
		return 1
	else:
		return number * factorial(number - 1)
