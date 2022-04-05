#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}
exports.addMeMaybe = addMeMaybe;
