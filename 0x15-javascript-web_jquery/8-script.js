$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function(data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    movies.forEach(function(movie) {
      const li = $('<li></li>').text(movie.title);
      listMovies.append(li);
    });
  });
});
