$(function(){
    $(".for_show_filters").click(function(){
        if ($(".filters").hasClass("show_filters")){
            $(".filters").removeClass("show_filters");
        } else {
            $(".filters").addClass("show_filters");
        }
    });
});
