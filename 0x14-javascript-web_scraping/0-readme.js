#!/usr/bin/node
// This script reads and prints the content of a file.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, f) {
  if (err) {
    return console.error(err);
  }
  console.log(f);
});
