#!/usr/bin/node

// Checks command line for arguments
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
