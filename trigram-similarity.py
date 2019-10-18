# coding=utf-8

import re
import sys

def similarity(first, second):
	if first.lower() == second.lower():
		return 1
	
	firstTrigrams = getTrigrams(first)
	secondTrigrams = getTrigrams(second)
	
	intersection = secondTrigrams.intersection(firstTrigrams)
	totalTrigrams = firstTrigrams.union(secondTrigrams)
	similarity = float((len(intersection) / len(totalTrigrams)))
	print("------------------")
	print("First: ", first)
	print("Second: ", second)
	print("Similarity: ", similarity)
	print("------------------")
	
	
def getTrigrams(input):
	PREFIX = "  "
	POSTFIX = " "
	lowerCase = input.lower()
	formatted = re.sub("[^a-zA-Z0-9áéíóúüñ¿¡]", " ", lowerCase)
	doubleSpaced = re.sub(" ", "  ", formatted)
	newWord = PREFIX + doubleSpaced + POSTFIX
	trigrams = set()
	for iterator in  range(len(newWord)-2):
		trigram = newWord[iterator:iterator+3]
		if isValid(trigram):
			trigrams.add(trigram)
	return trigrams
		
def isValid(trigram):
	return not(bool(re.match("[\w\d]\s+[\w\d]*", trigram))) and not(bool(re.match("\s\s\s", trigram)))

if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.exit("first input is needed")
	
	if len(sys.argv) == 2:
		sys.exit("second input is needed")
	
	first = sys.argv[1]
	second = sys.argv[2]
	similarity(first, second)