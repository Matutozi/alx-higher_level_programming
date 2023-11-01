#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  let count = 0;
  const bodyObj = JSON.parse(body).results;

  for (let i = 0; i < bodyObj.length; i++) {
    const a = bodyObj[i].characters.find((c) => {
      return c.match(/18/);
    });
    if (a !== undefined) {
      count++;
    }
  }

  console.log(count);
});
