#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
