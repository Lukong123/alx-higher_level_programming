$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(response) {
    for (let i = 0; i < response.results.length, i++){
	$('UL#list_movies').append(`<li>${response.results[i].title}</li>`);
    }
});

