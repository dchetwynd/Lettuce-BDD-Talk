from lettuce import *

@step(r'I have a first number of ([+-]?\d+)')
def first_number(step, number):
	world.first_operand = int(number)

@step(r'I have a second number of ([+-]?\d+)')
def second_number(step, number):
	world.second_operand = int(number)

@step(r'I add the two numbers together')
def add_numbers(step):
	world.result = world.first_operand + world.second_operand

@step(r'I should get a result of ([+-]?\d+)')
def result(step, result):
	expected = int(result)
	assert world.result == expected, "Expected %d but got %d" % (expected, world.result)

@step(r'I multiply the two numbers together')
def multiply_numbers(step):
	world.result = world.first_operand * world.second_operand
