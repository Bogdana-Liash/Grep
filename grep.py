#!/usr/bin/env python3

import sys

exitCode = 1
if len(sys.argv) != 2:
	print ('Error. Please write one argument.')
	sys.exit(exitCode)

searchString = sys.argv[1]
lenghtSearchString = len(searchString)


def getIndex(line, subString, searchPosition):
	lengthWithoutNewLine = len(line)
	validSearchLength = lengthWithoutNewLine - len(subString)
	
	if searchPosition > validSearchLength:
		return None

	for i in range(searchPosition, validSearchLength):
		if match(line, subString, i):
			return i

	return None


def match(line, subString, mainLineIndex):
	for i in range(len(subString)):
		if subString[i] != line[mainLineIndex + i]:
			return False
	return True
			

def searchHighlightSubstring(line, subString):
	arrayIndexToHighlight = []
	lenghtSubstr = len(subString)
	lengthLine = len(line)-1

	index = getIndex(line, subString, 0)
	while index != None:
		arrayIndexToHighlight.append(index)
		index = getIndex(line, subString, index + lenghtSubstr)

	return arrayIndexToHighlight


def setColorHighlight(line, arr, searchString):
	highLightedLine = ''
	position = 0
	colorHighlight = '\033[91m'
	colorDefault = '\033[0m'
	for shitIndex in arr:
		highLightedLine = highLightedLine \
						+ line[position:shitIndex] \
						+ colorHighlight \
						+ searchString \
						+ colorDefault		
		position = shitIndex + len(searchString)

	highLightedLine = highLightedLine + line[position:]
	return highLightedLine


for line in sys.stdin:
	highlightArray = searchHighlightSubstring(line, searchString)

	if len(highlightArray) != 0:
		string = setColorHighlight(line, highlightArray, searchString)
		print(string, end='')
		exitCode = 0

sys.exit(exitCode)