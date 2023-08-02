$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url, function(data) {
    $('#character').text(data.name); // Update the text of the <div> with the character name
  });
});
