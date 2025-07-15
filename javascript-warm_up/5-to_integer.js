#!/usr/bin/node
const num = process.argv[2];
const convertedNum = parseInt(num);

if (isNaN(convertedNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', convertedNum);
}
