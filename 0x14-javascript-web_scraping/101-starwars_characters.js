#!/usr/bin/node
// This script prints all characters of a Star Wars movie
// Display one character name by line in the same order of
// the list “characters” in the /films/ response
const axios = require('axios');
axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`)
  .then(res => {
    res.data.characters.forEach(link => {
      axios.get(link)
        .then(res => console.log(res.data.name));
    });
  })
  .catch(err => {
    console.log('Error:', err);
  });
