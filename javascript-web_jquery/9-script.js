$.get('https://stefanbohacek.com/hellosalut/?lang=f', function (data) {
  $('DIV#hello').html(data.hello);
});
