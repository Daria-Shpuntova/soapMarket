$(function(){
    $(".icon_menu").click(function(){
        if ($(".menu_toshow").hasClass("show_menu")){
            $(".menu_toshow").removeClass("show_menu");
        } else {
            $(".menu_toshow").addClass("show_menu");
        }
    });
});