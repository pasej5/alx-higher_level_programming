#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (!isNaN(num1) && !isNaN(num2)) {
  add(num1, num2);
} else {
  console.log('Invalid input. Please provide two valid integers.');
}
