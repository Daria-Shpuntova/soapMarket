$(document).ready(function() {
    totalPrice()
});

$(document).ajaxComplete(function() {
    totalPrice();
});

function totalPrice() {
    const prodPrice = document.querySelectorAll('.product_price');
    const prodQuantity = document.querySelectorAll('.product_quantity');

    let sumPrice = 0;
    let sumQuantity = 0;

    prodPrice.forEach(function(price) {
        sumPrice += Number(price.textContent)
    });

    let productPriceAll = document.getElementById('product_price_all');
    productPriceAll.innerHTML = sumPrice;

    prodQuantity.forEach(function(price) {
        sumQuantity += Number(price.textContent)
    });

    let productQuantityAll = document.getElementById('product_quantity_all');
    productQuantityAll.innerHTML = sumQuantity;
};




//document.addEventListener("DOMContentLoaded", function() {
//    const prodPrice = document.querySelectorAll('.product_price');
//    const prodQuantity = document.querySelectorAll('.product_quantity');
//
//    let sumPrice = 0;
//    let sumQuantity = 0;
//
//    prodPrice.forEach(function(price) {
//        sumPrice += Number(price.textContent)
//    });
//
//    let productPriceAll = document.getElementById('product_price_all');
//    productPriceAll.innerHTML = sumPrice;
//
//    prodQuantity.forEach(function(price) {
//        sumQuantity += Number(price.textContent)
//    });
//
//    let productQuantityAll = document.getElementById('product_quantity_all');
//    productQuantityAll.innerHTML = sumQuantity;
//});
//
//