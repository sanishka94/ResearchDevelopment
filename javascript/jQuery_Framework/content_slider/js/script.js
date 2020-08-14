$(document).ready(function(){
    // set speed
    var speed = 500;    // fade speed
    var autoswitch = true;  // auto slider option
    var autoswitch_speed = 4000;    // auto slider speed

    // Add inital active class
    $('.slide').first().addClass('active');

    // Hide all slides
    $('.slide').hide();

    // SHow first slide
    $('.active').show();

    // Next Handler
    $('#next').on('click', nextSlide);

    // Prev Handler
    $('#prev').on('click', prevSlide);

    // Auto Slider Handler
    if(autoswitch){
        setInterval(() => nextSlide(), autoswitch_speed);
    }

    // Switch to the next slide
    function nextSlide(){
        $('.active').removeClass('active').addClass('oldActive');
        if($('.oldActive').is(':last-child')){
            $('.slide').first().addClass('active');
        } else {
            $('.oldActive').next().addClass('active');
        }
        $('.oldActive').removeClass('oldActive');
        $('.slide').fadeOut(speed);
        $('.active').fadeIn(speed);
    }

    // Switch to previous slide
    function prevSlide(){
        $('.active').removeClass('active').addClass('oldActive');
        if($('.oldActive').is(':first-child')){
            $('.slide').last().addClass('active');
        } else {
            $('.oldActive').prev().addClass('active');
        }
        $('.oldActive').removeClass('oldActive');
        $('.slide').fadeOut(speed);
        $('.active').fadeIn(speed);
    }
});