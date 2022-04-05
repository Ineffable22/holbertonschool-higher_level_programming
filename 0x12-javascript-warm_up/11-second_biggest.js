#!/usr/bin/node
const num = process.argv.sort((a, b) => (a - b));
if (process.argv.length <= 2) console.log(0);
else console.log(num[process.argv.length - 2]);
