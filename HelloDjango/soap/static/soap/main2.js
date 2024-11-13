$(document).ready(function() {
    console.log($('.prod'),'prod')
    $('.prod').each(function(){
        console.log($(this)[0],'22');
        console.log($(this).children('form').children('select').next()[0], 'id_product')

        console.log($(this)[0].classList[1], 34);
        let num=$(this)[0].classList[1];
        console.log(num.slice(2), 35);

        let num2 = num.slice(2)

        var options = $(this).children('form').children('select').children('option');
        console.log(options, 'options')

        for (var i = 0; i < options.length; i++) {
            if (options[i].text === num ) {
                options[i].setAttribute("selected", "selected");
                console.log(options[i], 'options[i]')
                   break;
            }
        }
    });
});