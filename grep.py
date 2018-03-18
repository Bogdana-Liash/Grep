#!/usr/bin/env python3

import sys

def main():
	exitCode = 1
	if len(sys.argv) != 2:
		print ('Error. Please write one argument.')
		sys.exit(exitCode)

	searchString = sys.argv[1]
	lenghtSearchString = len(searchString)

	for line in sys.stdin:
		highlightArray = searchHighlightSubstring(line, searchString)

		if len(highlightArray) != 0:
			string = setColorHighlight(line, highlightArray, searchString)
			print(string, end='')
			exitCode = 0

	sys.exit(exitCode)


def getIndex(line, subString, searchPosition):
	"""Starts search subString in line from searchPosition, if subString is longer than line tail after searchPosition.

	Args:
		line(string): line for search.
		subString(string): searched string.
		searchPosition(int): index to start search from.

	Returns:
		None if line tail after searchPosition shorter than searchPosition or nothing found.
		Index(int) inside line, where found substring starts.
	"""
	lengthWithoutNewLine = len(line)-1
	validSearchLength = lengthWithoutNewLine - len(subString)
	
	if searchPosition > validSearchLength:
		return None

	for i in range(searchPosition, validSearchLength+1):
		if match(line, subString, i):
			return i

	return None


def match(line, subString, mainLineIndex):
	"""Compares subString to line from mainLineIndex.

	Args:
		line(string): line for search.
		subString(string): searched string.
		mainLineIndex(int): index from line, which needs to start search subString.

	Returns:
		True if search is successful, False otherwise.
	"""
	for i in range(len(subString)):
		if subString[i] != line[mainLineIndex + i]:
			return False
	return True
			

def searchHighlightSubstring(line, subString):
	"""Fills array with index(-es) from line, where found substring(-s) starts.

	Args:
		line(string): line for search.
		subString(string): searched string.

	Returns:
		full array, if successful search, empty if nothing found.
	"""
	arrayIndexToHighlight = []
	lenghtSubstr = len(subString)
	lengthLine = len(line)-1

	index = getIndex(line, subString, 0)
	while index != None:
		arrayIndexToHighlight.append(index)
		index = getIndex(line, subString, index + lenghtSubstr)

	return arrayIndexToHighlight


def setColorHighlight(line, arr, searchString):
	"""Returns line with highlighted found substring(-s). Adds color codes for bash.

	Args:
		line(string): line for search.
		arr(array): index(-es) inside line, where found substring(-s) starts.
		searchString(string): searched string.
	"""
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


if __name__ == "__main__":
    main()