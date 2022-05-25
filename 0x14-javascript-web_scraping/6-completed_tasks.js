#!/usr/bin/node
// this funciton prints the number of task completed by a particular user ID;

const request = require('request');
const count = {};

request(process.argv[2], function(err, response, body) {
    if (err) {
	console.log(err);
    } else {
	const todos = JSON.parse(body);
	for (let i = 0; i < todos.length; i++) {
	    for (let j = 0; j < todos[i].userId.length; j++) {
		if (todos[i].userId[j].completed === true) {
		    count ++;
		}
	    }
	}
    }
    console.log(count);
});
