$(document).ready(function() {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.get(url, function(data) {
    $('#hello').text(data.hello); // Update the text of the <div> with the translation of "hello"
  });
});
