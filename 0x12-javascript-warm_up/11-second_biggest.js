#!/usr/bin/node
const num = process.argv.splice(2).map((z) => parseInt(z)).sort((a, b) => (a - b));
if (num.length <= 1) console.log(0);
else console.log(num[process.argv.length - 2]);
