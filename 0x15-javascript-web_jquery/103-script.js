$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();

    if (languageCode !== '') {
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        type: 'GET',
        data: { lang: languageCode },
        success: function(response) {
          $('#hello').text(response.hello);
        }
      });
    }
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
