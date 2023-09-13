#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    let row = '';
    for (let i = 0; i < this.size; i++) {
      row += c;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
