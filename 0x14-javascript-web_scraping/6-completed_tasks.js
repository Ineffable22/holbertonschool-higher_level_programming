#!/usr/bin/node
// This script computes the number of tasks completed by user id.
const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    const obj = {};
    res.data.forEach(data => {
      if (data.completed === true) {
        if (obj[data.userId] === undefined) {
          obj[data.userId] = 1;
        } else {
          obj[data.userId]++;
        }
      }
    });
    console.log(obj);
  })
  .catch(err => {
    console.log('Error:', err);
  });
