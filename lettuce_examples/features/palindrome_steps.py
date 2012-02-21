from lettuce import *

@step(r'the input string (\w+)')
def input_string(step, string):
	world.input_string = string

@step(r'I ask whether it is a palindrome')
def check_palindrome(step):
	world.palindrome = is_palindrome(world.input_string)

@step(r'I should get the response (\w+)')
def palindrome_result(step, result):
	assert world.palindrome == result

def is_palindrome(input_string):
	reversed_string = input_string[::-1]
	if (input_string == reversed_string):
		return 'Yes'
	else:
		return 'No'
