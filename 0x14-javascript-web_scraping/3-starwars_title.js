#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request(link, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
