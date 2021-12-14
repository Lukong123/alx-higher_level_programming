#!/usr/bin/node
/* increments */
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
