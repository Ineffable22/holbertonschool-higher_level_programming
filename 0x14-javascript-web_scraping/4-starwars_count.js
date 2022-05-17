#!/usr/bin/node
// This script prints the number of movies where
// the character “Wedge Antilles” is present.
const axios = require('axios');
const ID = 'https://swapi-api.hbtn.io/api/people/18/';
let total = 0;

axios.get(process.argv[2])
  .then(res => {
    const films = res.data.results ? res.data.results : [];
    const size = films.length;
    for (let i = 0; i < size; i++) {
      if (films[i].characters.includes(ID) === true) total++;
    }
    console.log(total);
  })
  .catch(err => {
    console.log('error:', err);
  });
