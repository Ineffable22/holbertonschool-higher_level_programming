#!/usr/bin/node
exports.nbOccurences = (list, elm) => list.reduce((acm, value) => value === elm ? acm + 1 : acm, 0);

/*
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (let i of list) {
    if (i == searchElement) sum += 1;
  } return (sum);
}
*/
