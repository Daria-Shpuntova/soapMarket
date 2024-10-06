var btn = $('#button');
var menu = $('.menu');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
    menu.addClass('show_menu_scroll');
  } else {
    btn.removeClass('show');
    menu.removeClass('show_menu_scroll');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});