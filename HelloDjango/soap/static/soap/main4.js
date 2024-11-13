//$(document).ready(function() {
//    console.log($('.prod'),'prod')
//    $('.prod').each(function(){
//        console.log($(this)[0],'22');
//        console.log($(this)[0].classList[1], 34);
//
//        var options = $(this).children('div').children('form').children('select')[0].options
//        console.log($(this).children('div').children('form').children('select')[0].options, 'id_product')
//
//
//        let num=$(this)[0].classList[1];
//        console.log(num.slice(2), 35);
//        let num2 = num.slice(2)
//
//        for (var i = 0; i < options.length; i++) {
//            console.log(options[i].value, 'options[i].value')
//
//            if (options[i].value === num2 ) {
//                options[i].setAttribute("selected", "selected");
//                options[i].selected = true;
//                console.log(options[i], 'options[i]')
//                   break;
//            }
//        }
//    });
//});

//document.addEventListener("DOMContentLoaded", function() {
//  const prodDivs = document.querySelectorAll('.prods .prod');
//  prodDivs.forEach(function(div) {
//    const pId = div.classList[1].split('_')[1];
//    const selectElement = document.createElement('select');
//    selectElement.name = 'product';
//    selectElement.innerHTML = `<option value="${pId}">${pId}</option>`;
//    div.querySelector('.price_basket form').prepend(selectElement);
//  });
//});


//document.addEventListener('DOMContentLoaded', function() {
//    var divs = document.querySelectorAll('.prods .prod');
//
//    divs.forEach(function(div) {
//        var productId = div.classList[1].split('_')[1]; // Получить id из класса div
//        var select = div.querySelector('select[name="product"]'); // Найти соответствующий элемент <select>
//
//        // Установить "selected" для элемента <option> с нужным значением
//        var option = select.querySelector('option[value="' + productId + '"]');
//        if (option) {
//            option.selected = true;
//        }
//    });
//});

document.addEventListener('DOMContentLoaded', function() {
    var divs = document.querySelectorAll('.prods .prod');

    divs.forEach(function(div) {
        var productId = div.classList[1].split('_')[1]; // Получить id из класса div
        var select = div.querySelector('select[name="product"]'); // Найти соответствующий элемент <select>

        if (select) { // Добавляем проверку на существование select элемента
            // Установить "selected" для элемента <option> с нужным значением
            var option = select.querySelector('option[value="' + productId + '"]');
            if (option) {
                option.selected = true;
            }
        }
    });
});