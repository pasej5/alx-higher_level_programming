#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 3) {
  console.log('Usage: node yourScriptName.js <filename>');
  process.exit(1);
}

const filename = process.argv[2];

fs.readFile(filename, 'utf8', function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
