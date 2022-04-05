#!/usr/bin/node
// function add (a, b) {
//  console.log(parseInt(a) + parseInt(b));
//  } add(process.argv[2], process.argv[3]);*/
// const add = (a, b) => console.log(parseInt(a) + parseInt(b));
// add(process.argv[2], process.argv[3])
((a = process.argv[2], b = process.argv[3]) => console.log(parseInt(a) + parseInt(b)))();
