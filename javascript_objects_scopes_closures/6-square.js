#!/usr/bin/node
const SQUARE = require('./5-square');
module.exports = class Square extends SQUARE {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let j = 0;
      for (j = 0; j < this.height; j++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
