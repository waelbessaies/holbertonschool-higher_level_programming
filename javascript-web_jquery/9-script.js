$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (displayvalue) {
  $('DIV#hello').html(displayvalue.hello);
});
