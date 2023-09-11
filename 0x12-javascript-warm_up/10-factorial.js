#!/usr/bin/node

// Prints factorial of number
function factorial (n) {
  if (n === 0 || isNaN(Number(arg))) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const arg = process.argv[2];
console.log(factorial(parseInt(arg)));
