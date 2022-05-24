#!/usr/bin/node
// this script prints the status code of a GET request

const request = require('request');
request(process.argv[2], function(err, response) {
    if (err) {
	return console.log(err);
    }
    console.log('code:', response.statusCode);
});

