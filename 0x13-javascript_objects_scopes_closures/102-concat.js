#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const fileA = fs.readFileSync(args[2], 'utf-8', (err, data) => {
  if (err) throw err;
});
const fileB = fs.readFileSync(args[3], 'utf-8', (err, data) => {
  if (err) throw err;
});
const fileC = fileA + fileB;
fs.writeFileSync(args[4], fileC, 'utf-8', (err, data) => {
  if (err) throw err;
});
