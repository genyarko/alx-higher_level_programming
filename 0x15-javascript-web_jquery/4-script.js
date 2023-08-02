$(document).ready(function() {
  $('#toggle_header').click(function() {
    const headerElement = $('header');
    if (headerElement.hasClass('red')) {
      headerElement.removeClass('red');
      headerElement.addClass('green');
    } else if (headerElement.hasClass('green')) {
      headerElement.removeClass('green');
      headerElement.addClass('red');
    } else {
      headerElement.addClass('red');
    }
  });
});
