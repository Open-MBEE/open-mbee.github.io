$('#nav-container').load('navbar.html', function() {
  var title = $('title').text().substring(11);
  $('#navbar-title').html(title);
  if (title == 'About') {
    $('#about').addClass('active');
  }
  if (title == 'Contribute') {
    $('#contribute').addClass('active');
  }
  if (title == 'Products') {
    $('#products').addClass('active');
  }
});

/*Add footer to each page, should reflect nav eventually*/
$('#footer-container').load('footer.html', function() {
});