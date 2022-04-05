#!/usr/bin/node
let a = 0;
exports.logMe = function (item) {
  console.log(a + ': ' + item);
  a++;
};
