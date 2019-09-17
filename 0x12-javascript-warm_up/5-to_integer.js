#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(Number(process.argv[2])));
}
