$(document).ready(function() {
   $('form[id^="BasketForm"]').submit(function(event) {
   event.preventDefault();
   $.ajax({
       url: $(this).attr('action'),
       type: $(this).attr('method'),
       data: $(this).serialize(),
       success: function() {
               $('#bask_num').load(window.location.href + " #bask_num" );
               $("#BasketForm").trigger('reset');
           },
       error: function() {
           alert('Что-то пошло не так');
       }
       });
   });
})