$('#nav-container').load('navbar.html', function() {
  $('#nav-title').html($('title').text().substring(11));
});