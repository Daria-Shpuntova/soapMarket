function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function prov(product_id, quantity, product_quantity, product_name){
    if ((Number(quantity) > Number(product_quantity))){
        console.log(33)
        alert('К сожалению, '+ product_name +' максимально  доступно для заказа ' + product_quantity + 'шт.')

    } else {
        console.log(15)
        updateQuantity(product_id, quantity)
    }
}


function updateQuantity(product_id, quantity) {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url: "/update_quantity/",
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: {
            product_id: product_id,
            quantity: quantity
        },
        success: function(response) {
            // обновление информации о корзине на странице
            console.log('+');
            $("#table").load(location.href + " #table");

            console.log('++')
        },
        error: function(xhr, status, error) {
            console.log('Ошибка при обновлении количества товара в корзине: ' + error);
        }
    });

}

function delete_prod(product_id) {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
//        url: '/update_quantity/',
        url: "/delete_prod/",
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: {
            product_id: product_id
        },
        success: function(response) {
            // обновление информации о корзине на странице
            console.log('+-');
            $("#table").load(location.href + " #table");

            console.log('+-+')
        },
        error: function(xhr, status, error) {
            console.log('Ошибка при удалении товара в корзине: ' + error);
        }
    });
}

//function updateQuantity(product_id, quantity) {
//    var csrftoken = getCookie('csrftoken');
//    $.ajax({
//        url: '/',
//        type: 'POST',
//        headers: {
//            'X-CSRFToken': csrftoken
//        },
//        data: {
//            product_id: product_id,
//            quantity: quantity
//        },
//        success: function(response) {
//            // обновление информации о корзине на странице
//            console.log('+')
//        },
//        error: function(xhr, status, error) {
//            console.log('Ошибка при обновлении количества товара в корзине: ' + error);
//        }
//    });
//}