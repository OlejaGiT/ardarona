$(function() {

    var header = $("#header"),
        introH = $("#intro").innerHeight();
        contentH = $("#content").innerHeight();
        scrollOffset = $(window).scrollTop();

        checkScroll(scrollOffset);

    $(window).on("scroll", function() {

        scrollOffset = $(this).scrollTop();

        checkScroll(scrollOffset);
        
    });

    
        $('.navv a').each(function () {
            var location = window.location.href;
            var link = this.href; 
            if(location == link) {
                $(this).addClass('active');
            }
        });


    function checkScroll(scrollOffset) {
        if( scrollOffset >= introH ) {
            header.addClass("fixed");
        } else {
            header.removeClass("fixed");
        }
        if( scrollOffset > contentH ) {
            header.addClass("fixed");
        } else {
            header.removeClass("fixed");
        }
    }


    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();
        var $this = $(this),
            blockId = $this.data('scroll'),
            blockOffset = $(blockId).offset().top;


            $("#nav a").removeClass("active");
            $this.addClass("active");




        $("html, body").animate({
            scrollTop: blockOffset
        }, 250);

    });

    $("#nav_toggle").on("click", function(){
        $(this).toggleClass("active")
        $("#nav").toggleClass("active")
        $("#header").addClass("fixed")
        


    });

    $("[data-collapse]").on("click", function(event){
        event.preventDefault();

        var $this=$(this),
            blockId = $this.data('collapse');


        $this.toggleClass("active"),
        $(blockId).slideToggle();


    });

    

});