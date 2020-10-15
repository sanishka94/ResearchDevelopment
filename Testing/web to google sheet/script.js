$( document ).ready(function() {
    $("#send").on("click", function() {
        var data = {
            "name" : "sanihka",
            "email" : "testing@test.com"
        }

        $.ajax({
            url : "https://script.google.com/macros/s/AKfycbwLO4ApRj8hxh6SzJ4VAByCfg007NHNIrAK3YUbk0PuAvzCMZA/exec",
            data : data,
            type : "post",
            jsonp: "callback",
            dataType : "jsonp",
            success : function(e){
                console.log("Data sent");
            },
            error : function(e){
                console.log(e);
            }
        });
    });
});

