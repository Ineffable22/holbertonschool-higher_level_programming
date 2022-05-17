#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file.
const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2])
  .then(res => {
    fs.writeFile(process.argv[3], res.data, err => {
      if (err) {
        return console.log(err);
      }
    });
  });
