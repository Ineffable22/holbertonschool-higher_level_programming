#!/usr/bin/node
const num = process.argv.sort();
if (isNaN(num)) console.log('0');
else console.log(num[process.argv.length - 2]);
