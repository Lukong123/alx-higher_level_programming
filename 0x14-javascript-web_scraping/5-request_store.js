#!/usr/bin/node
// this script gets the content of a webpage and store it in a file

const request = require('request');
const fs = require('fs');
request(process.argv[2], function(err, response, body) {
    if (err) {
	console.log(err)
    } else {
	fs.appendFile(process.argv[3], body, 'utf-8', function(err) {
	    if (err) {
		console.log(err);
	    }
	});
    }
});
