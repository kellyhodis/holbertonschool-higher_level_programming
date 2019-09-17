#!/usr/bin/node
let max_ = Number.NEGATIVE_INFINITY;
let secondMax = max_;
if (process.argv.length === 2 | process.argv.length === 3) { console.log(0); } else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max_) {
      secondMax = max_;
      max_ = process.argv[i];
    }
  }
  console.log(secondMax);
}
