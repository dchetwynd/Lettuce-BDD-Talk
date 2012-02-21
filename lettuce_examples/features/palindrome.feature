Feature: Palindromes
	As a simple string example
	So that I can demonstrate lettuce
	I want to know whether a given string is a palindrome

	Scenarios: Palindrome examples
		Given the input string <input_string>
		When I ask whether it is a palindrome
		Then I should get the response <result>
	
	Examples:
	  | input_string | result |
	  | wow          | Yes    |
	  | redder       | Yes    |
	  | rudder       | No     |
	  | level        | Yes    |
	  | lever        | No     |		
