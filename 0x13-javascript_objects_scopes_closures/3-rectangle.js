#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        let x_ = '';
        for (let i = 0; i < this.width; i++) {
          x_ += 'X';
        }
        for (let j = 0; j < this.height; j++) {
          console.log(x_);
        }
      };
    }
  }
}
module.exports = Rectangle;
