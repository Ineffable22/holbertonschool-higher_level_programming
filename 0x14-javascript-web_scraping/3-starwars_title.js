#!/usr/bin/node
// This script prints the title of a Star Wars movie where
// the episode number matches a given integer.
const axios = require('axios');
const ID = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${ID}`)
  .then(res => {
    console.log(res.data.title);
  });
