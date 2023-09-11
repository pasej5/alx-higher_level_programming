#!/usr/bin/node

const size = process.argv[2];

if (!isNaN(size) && Number.isInteger(Number(size))) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
