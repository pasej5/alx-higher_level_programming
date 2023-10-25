#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.agv[3], error => {
   if (error) console.log(error);
});
