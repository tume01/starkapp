/* Scroll to top functionality */
$(function() {
        // Get link
        var link = $('#to-top');
        var windowW = window.innerWidth
        || document.documentElement.clientWidth
        || document.body.clientWidth;

        $(window).scroll(function() {
            // If the user scrolled a bit (150 pixels) show the link in large resolutions
            if (($(this).scrollTop() > 150) && (windowW > 991)) {
              link.fadeIn(100);
            } else {
              link.fadeOut(100);
            }
          }); 

        // On click get to top
        link.click(function() {
          $(".site-nav-sub").removeClass("active");
          $('#inicio').addClass( "active"); 
          $('html, body').animate({scrollTop: 0}, 500);
          return false;
        });
      });

$.fn.scrollBottom = function() { 
    return $(document).height() - this.scrollTop() - this.height(); 
};

$(function(){

  $(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    var scroll2 = $(window).scrollBottom();
  //$(".site-nav").html(scroll2);
  if (scroll < 517) {
    $(".site-nav-sub").removeClass("active");
    $("#inicio").addClass("active");
  }else{
    if (scroll >= 517 && scroll < 1339) {
      $('.site-nav-sub').removeClass("active");
      $("#catalogo").addClass("active");        
    } else {
      if(scroll >= 1339 && scroll < 1958){
        $(".site-nav-sub").removeClass("active");
        $("#equipo").addClass("active");
      }else{
        if(scroll >= 1958 && scroll2 >= 650){
          $(".site-nav-sub").removeClass("active");
          $("#cursos").addClass("active");
        }else{
          if(scroll >= 1958 && scroll2 < 650){
            $(".site-nav-sub").removeClass("active");
            $("#contacto").addClass("active");
          }
          
        }
      }
    }
  }
});
});