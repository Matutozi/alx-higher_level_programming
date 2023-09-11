#!/usr/bin/node

// Prints a square number of characters for a given number
const k = process.argv[2];

if (isNaN(Number(k))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < k; i++) {
    let output = 'X';
    for (let n = 1; n < k; n++) {
      output += 'X';
    }
    console.log(output);
  }
}
