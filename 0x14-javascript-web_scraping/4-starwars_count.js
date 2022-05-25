#!/usr/bin/node

// this script prints the number of movies wheere the character Wedge Antilles is present.

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function(err, response, body) {
    if (err){
	console.log(err);
    } else {
	const movies = JSON.parse(body).results;
	for (let i = 0; i < movies.length; i++) {
	    for (let j = 0; j < movies[i].characters.length; j++) {
		if (movies[i].characters[j].search('/18/') > 0) {
		    count++;
		}
	    }
	}
    }
    console.log(count);
});

