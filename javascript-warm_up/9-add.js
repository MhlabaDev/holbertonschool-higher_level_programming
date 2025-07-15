#!/usr/bin/node
// Script that adds two integers with exact test case matching

function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
