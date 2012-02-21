Feature: Simple maths
	As a maths dunce
	So that I can use simple maths in my life
	I need calculations to be performed for me

	Scenario: Adding two numbers together
		Given I have a first number of <first_number>
		And I have a second number of <second_number>
		When I add the two numbers together
		Then I should get a result of <result>
	
	Examples:
	  | first_number | second_number | result |
	  | 50           | 70            | 110    |
	  | 40           | 0             | 40     |
	  | 80           | -20           | 60     |
	
	Scenario: Multiplying two numbers together
		Given I have a first number of <first_number>
		And I have a second number of <second_number>
		When I multiply the two numbers together
		Then I should get a result of <result>
	
	Examples:
	  | first_number | second_number | result |
	  | 15           | 5             | 75     |
	  | 0            | 9             | 0      |
	  | 8            | 0             | 0      |
	  | -3           | 12            | -36    |
	  | -6           | -13           | 78     |
