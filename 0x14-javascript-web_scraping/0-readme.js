#!/usr/bin/node
const readMe = require('redMe');
readMe.readFile(process.argv[2]. 'utf8', function (error, content) {
console.log(error || content);
});

