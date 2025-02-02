jQuery(document).ready(($) => {

    $('#slider1, #slider2, #slider3').owlCarousel({
        loop: true,
        margin: 20,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false,
                autoplay: true,
            },
            600: {
                items: 3,
                nav: true,
                autoplay: true,
            },
            1000: {
                items: 5,
                nav: true,
                loop: true,
                autoplay: true,
            }
        }
    });
    

// Get product quantity add/remove count

    $('.plus-cart').click(()=> {
        let p_id = $('.pluscart-btn').attr('pid').toString();
        let ele = document.querySelector('#quantity');
        let amount = document.querySelector('#amount');
        let totalAmount = document.querySelector('#total_amount')
        $.ajax({
            url : "/pluscart/",
            type:"GET",
            data : {
                prod_id : p_id
            },
            success: function (data){
                console.log('Hello', data)
                ele.innerText = data.quantity
                amount.innerText = data.amount
                totalAmount.innerText = data.total_amount               
            }
        });
    });


    $('.minus-cart').click(()=> {
        let p_id = $('.minuscart-btn').attr('pid').toString();
        let ele = document.querySelector('#quantity');
        let amount = document.querySelector('#amount');
        let totalAmount = document.querySelector('#total_amount')
        $.ajax({
            url : "/minuscart/",
            type:"GET",
            data : {
                prod_id : p_id
            },
            success: function (data){
                console.log('Hello', data)
                ele.innerText = data.quantity
                amount.innerText = data.amount
                totalAmount.innerText = data.total_amount               
            }
        });
    });


    $('.remove-cart').click(()=> {
        let p_id = $('.remove-cart-btn').attr('pid').toString();
        let amount = document.querySelector('#amount');
        let totalAmount = document.querySelector('#total_amount')
        let productRow = document.querySelector('.prod-row')
        $.ajax({
            url : "/removecart/",
            type:"GET",
            data : {
                prod_id : p_id
            },
            success: function (data){
                amount.innerText = data.amount
                totalAmount.innerText = data.total_amount    
                productRow.remove()

            }
        });
    });













});