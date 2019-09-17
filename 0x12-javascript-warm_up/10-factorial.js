#!/usr/bin/node
function factorial (x) {
  if (x <= 1 | isNaN(x)) { return 1; }
  return x * factorial(x - 1);
}
console.log(factorial(process.argv[2]));
