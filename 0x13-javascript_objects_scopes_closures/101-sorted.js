#!/usr/bin/node
const dict = require('./101-data').dict;
const occurs = Object.keys(dict);
const newDict = {};
for (let i = 0; i < occurs.length; i++) {
  if (newDict[dict[occurs[i]]] === undefined) {
    newDict[dict[occurs[i]]] = [occurs[i]];
  } else {
    newDict[dict[occurs[i]]].push(occurs[i]);
  }
}
console.log(newDict);
