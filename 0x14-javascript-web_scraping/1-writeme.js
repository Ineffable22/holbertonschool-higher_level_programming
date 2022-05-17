#!/usr/bin/node
// This script writes a string to a file.
const fs = require('fs');
const content = process.argv[3];
fs.writeFile(process.argv[2], content, err => {
  if (err) {
    return console.log(err);
  }
});
