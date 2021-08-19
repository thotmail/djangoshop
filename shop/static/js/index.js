function cartUpdate(){
    if(Cookies.get("cart")){
        $("#cart").text("("+Object.keys($.parseJSON(Cookies.get("cart"))).length+")")
    }
    else{
        $("#cart").text("")
    }
}

$(document).ready(function(){
    cartUpdate()

    $("#addCart").click(function(){
        amt = Number($('#quantity').val())
        pk=$('#pk').text()

        if(!Cookies.get("cart")){
            cart={}
        }
        else{
            cart = $.parseJSON(Cookies.get("cart"))
        }
        if(amt>0){
            cart[pk]=amt
        }
        else{
            delete cart[pk]
        }
        if(Object.keys(cart).length > 0){
            console.log("cart="+JSON.stringify(cart)+";path='';samesite=strict;")
            document.cookie="cart="+JSON.stringify(cart)+";path=/;samesite=strict;"
        }
        else{
            Cookies.remove("cart")
        }
        cartUpdate()
    })

})