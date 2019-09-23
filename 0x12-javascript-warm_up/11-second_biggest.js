#!/usr/bin/node
if (process.argv.length === 2 | process.argv.length === 3) { console.log(0); } else {
  let max_ = process.argv[2];
  let secondMax = max_;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max_) {
      secondMax = max_;
      max_ = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > secondMax) {
      secondMax = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) === max_) {
      secondMax = max_;
    }
  }
  console.log(secondMax);
}
