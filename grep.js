//"use strict";

if ( process.argv.length != 3 ) {
	console.log('Error. Please write one argument.');
	return false;
}

const searchString = process.argv[2];
const lenghtSearchString = process.argv[2].length;

function getIndex(line, subString, searchPosition){
	let lengthWithoutZeroIndex = line.length;
	let validSearchLength = lengthWithoutZeroIndex - subString.length;

	if ( searchPosition > validSearchLength ) { return false; }
	
	for (let i = searchPosition; i <= validSearchLength; i++) {
		if ( match(line, subString, i) ) { return i; }
	}

	return false;
};

function match(line, subString, mainLineIndex){
	for (let i = 0; i < subString.length; i++) {
		if ( subString[i] != line[mainLineIndex + i] ) { return false; }		
	}
	return true;
};

function searchHighlightSubstring(line, subString){
	let arrayIndexToHighlight = [];
	let lenghtSubstr = subString.length;
	let lengthLine = line.length-1;
	
	let index = getIndex(line, subString, 0);	
	while ( index !== false  ) {
		arrayIndexToHighlight.push(index);
		index = getIndex(line, subString, index + lenghtSubstr);
	}

	return arrayIndexToHighlight;
};

function setColorHighlight(line, arr, searchString){
	let highLightedLine = '';
	let position = 0;
	const colorHighlight = '\033[91m';
	const colorDefault = '\033[0m';

	for (var i = 0; i < arr.length; i++) {
		highLightedLine = highLightedLine + line.slice(position, arr[i]) + colorHighlight + searchString + colorDefault;
		position = arr[i] + searchString.length;
	}
	
	highLightedLine = highLightedLine + line.slice(position);
	return highLightedLine;
};

let readline = require('readline');
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line){
    let highlightArray = searchHighlightSubstring(line, searchString);

    if (highlightArray.length != 0) {
    	let string = setColorHighlight(line, highlightArray, searchString);
    	console.log(string);
    }
});

return true;