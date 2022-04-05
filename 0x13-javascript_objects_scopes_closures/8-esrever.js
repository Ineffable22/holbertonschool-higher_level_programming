#!/usr/bin/node
exports.esrever = function (list) {
  const ls = [];
  list.forEach(value => ls.unshift(value));
  return (ls);
};
