$(document).ready(function(){
    $('#submit').on('click', function(){
        var name = $('#name').val();
        var shout = $('#shout').val();
        // var date = getDate();
        // var dataString = 'name='+name+'&shout='+shout+'&date='+date;
    
        // Validation
        if(name=='' || shout==''){
            alert('Please fill in your name and shout')
        } else {
            $.ajax({
                type:"POST",
                url:"../jsshoutbox/shoutbox.php",
                data: dataString,
                success: function(html){
                    $('#shouts ul').prepend(html);
                }
            });
        }
    
        return false;
    });
});

function getDate(){
    var date;
    date = new Date;
    date = date.getUTCFullYear() + 
}