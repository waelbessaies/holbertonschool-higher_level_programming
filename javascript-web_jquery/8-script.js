const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (title_movie) {
  for (let i = 0; i < title_movie.results.length; i++) {
    $('ul#list_movies').append(`<li>${title_movie.results[i].title}</li>`);
  }
});
