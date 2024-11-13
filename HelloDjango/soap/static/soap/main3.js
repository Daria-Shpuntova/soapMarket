$(document).ready(function() {
 //   console.log($('.prod'),'prod')
    $('.prod').each(function(){
//        console.log($(this)[0],'22');
        var productId = $(this)[0].classList[1].split('_')[1]
 //       console.log(productId,'23');

        var select = $(this)[0].querySelector('select[name="product"]');
 //       console.log(select,'select');

        if (select) { // Добавляем проверку на существование select элемента
            // Установить "selected" для элемента <option> с нужным значением
            var option = select.querySelector('option[value="' + productId + '"]');
  //          console.log(option,'option');
            if (option) {
                option.selected = true;
  //              console.log(option,'option.selected');
                option.setAttribute("selected", "selected");
            }
        }
    });
});

//       var options = $(this).children('div').children('form').children('select')[0].options
//       console.log($(this).children('div').children('form').children('select')[0].options, 'id_product')

//        for (var i = 0; i < options.length; i++) {
//            console.log(options[i].value, 'options[i].value')
//        }

//       console.log($(this).children('form').children('input').next()[0], 'id_product')

//       console.log($(this)[0].classList[1]);
//       let num=$(this)[0].classList[1];
//       console.log(num.slice(2));

//       let product = $(this).children('form').children('input').next()[0]
//       console.log($(this).children('form').children('input').next()[0].value, 'id_product2')

//       let num2 = num.slice(2)
//       product.value = num2

//       console.log(product.value, 'num2')
//    });
//});