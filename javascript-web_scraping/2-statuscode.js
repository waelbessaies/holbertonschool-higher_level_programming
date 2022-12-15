#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, resp) {
  if (err) {
    console.error('err', err);
  } else {
    console.log('code:', resp.statusCode);
  }
});
