#!/usr/bin/node

// to print text on a screen
const number = process.argv[2];

if (isNaN(Number(number))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
