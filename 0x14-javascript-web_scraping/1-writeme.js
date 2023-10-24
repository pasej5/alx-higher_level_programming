#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: node writeToFile.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', function (error) {
  if (error) {
    console.error('Error writing to the file:', error);
  } else {
    console.log('Content successfully written to the file.');
  }
});
