#!/usr/bin/node
// This script prints all characters of a Star Wars movie
const axios = require('axios');

axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(res => {
    res.data.characters.forEach(async (data) => {
      await axios.get(data)
        .then(res => {
          console.log(res.data.name);
        });
    });
  })
  .catch(err => {
    console.log('Error:', err);
  });
