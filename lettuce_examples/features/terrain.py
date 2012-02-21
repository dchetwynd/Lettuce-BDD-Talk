from lettuce import *

@before.all
def header():
	print ("Running all lettuce features")

@after.all
def footer(total):
	print ("Finished running lettuce features")
