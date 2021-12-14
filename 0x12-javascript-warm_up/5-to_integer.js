#!/usr/bin/node
// a script that prints My number: <first argument converted in integer>
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
