#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (!err) {
    const objs = JSON.parse(body);
    const completed = {};
    objs.forEach((obj) => {
      if (obj.completed && completed[obj.userId] === undefined) {
        completed[obj.userId] = 1;
      } else if (obj.completed) {
        completed[obj.userId] += 1;
      }
    });
    console.log(completed);
  }
});
