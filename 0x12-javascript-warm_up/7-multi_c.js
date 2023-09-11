#!/usr/bin/node

// Prints text a given number of times
const text = 'C is fun';
const k = process.argv[2];

if (isNaN(Number(k))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < k; i++) {
    console.log(text);
  }
}
