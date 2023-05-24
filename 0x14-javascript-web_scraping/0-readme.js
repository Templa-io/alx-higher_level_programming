#!/usr/bin/node

const fs = require('fs');

fs.readFile("cisfun.text", 'utf-8', function (err, result) {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
