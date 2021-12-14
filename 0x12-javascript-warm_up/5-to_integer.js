#!/usr/bin/node
/* converting to interger */
const myNum = Number.parseInt (process.argv[2], 10);
if (isNaN(myNum)) {
    console.log('Not a number');
} else {
    console.log ( `My number: ${myNum}`);
}
