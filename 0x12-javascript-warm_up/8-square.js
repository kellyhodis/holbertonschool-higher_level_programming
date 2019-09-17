#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  let x_ = '';
  for (let j = 0; j < Number(process.argv[2]); j++) {
    x_ += 'X';
  }
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log(x_);
  }
}
