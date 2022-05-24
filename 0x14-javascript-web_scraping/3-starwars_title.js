#!/usr/bin/node

// this script prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];
request(url, function(err, response, body) {
    if (err) {
	return console.log(err);
    } else {
	console.log(JSON.parse(body).title);
    }
});

