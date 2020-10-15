$( document ).ready(function() {
    $("#send").on("click", function() {
        var data = {
            "name" : "sani",
            "email" : "test@test.com"
        }

        $.ajax({
            // url : "https://docs.google.com/forms/d/e/1FAIpQLSfQygzAgJj_Fx0_dytWYBHpxH-YxYT8NMCaVbTC6nPL2dxXDw/formResponse?",
            // url : "https://docs.google.com/spreadsheets/d/15XxTW1lq8x4jNFBS0EI5lQbMmGTxyVR1GDYHcl9ZDtY",
            url : "https://script.google.com/macros/s/AKfycbwLO4ApRj8hxh6SzJ4VAByCfg007NHNIrAK3YUbk0PuAvzCMZA/exec",
            data : data,
            type : "post",
            jsonp: "callback",
            dataType : "jsonp",
            // crossDomain: true,
            // Access-Control-Allow-Origin: *,
            success : function(e){
                console.log("Data sent");
            },
            error : function(e){
                console.log(e);
            }
        });
    });
});

