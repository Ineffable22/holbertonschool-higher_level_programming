#!/usr/bin/node
// This script computes the number of tasks completed by user id.
const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    const dict = {};
    let tmp = 1;
    let ss = 1;
    res.data.forEach(data => {
      if (data.userId !== ss) tmp = 1;
      if (data.completed === true) dict[data.userId] = tmp++;
      ss = data.userId;
    });
    console.log(dict);
  })
  .catch(err => {
    console.log('Error:', err);
  });
