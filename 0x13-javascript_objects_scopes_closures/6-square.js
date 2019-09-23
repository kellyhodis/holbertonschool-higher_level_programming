#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);

    this.charPrint = function (c = 'X') {
      let x_ = '';
      for (let i = 0; i < this.width; i++) {
        x_ += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(x_);
      }
    };
  }
}

module.exports = Square;
