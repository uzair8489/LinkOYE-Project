$(function() {
    $(window).scroll(function() {
        var winTop = $(window).scrollTop();
        if (winTop >= 50) {
            $(".navbar").addClass("sticky-header");
        } else {
            $(".navbar").removeClass("sticky-header");
        }
    });
});
$('#banner').owlCarousel({
    loop: true,
    margin: 10,
    nav: false,
    dots: true,
    autoplay: true,
    autoplayTimeout: 5000,
    smartSpeed: 500,
    //autoplayHoverPause:true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }

});
$(document).ready(function() {
    jQuery(window).scroll(startCounter);
});

function startCounter() {
    var hT = jQuery('.love_counter').offset().top,
        hH = jQuery('.love_counter').outerHeight(),
        wH = jQuery(window).height();
    if (jQuery(window).scrollTop() > hT + hH - wH) {
        jQuery(window).off("scroll", startCounter);
        jQuery('.love_count').each(function() {
            var $this = jQuery(this);
            $this[0].innerText = $this[0].innerText.replace(' ', '');
            jQuery({
                Counter: 0
            }).animate({
                Counter: $this.text()
            }, {
                duration: 2000,
                easing: 'swing',
                step: function() {
                    if ($this.hasClass('with-percent')) {
                        $this.text(Math.ceil(this.Counter) + '%');
                    } else {
                        $this.text(Math.ceil(this.Counter));
                    }
                }
            });
        });
    }
}


$(document).ready(function() {
    jQuery(window).scroll(startCounter2);
});

function startCounter2() {
    var hT = jQuery('.love_counter2').offset().top,
        hH = jQuery('.love_counter2').outerHeight(),
        wH = jQuery(window).height();
    if (jQuery(window).scrollTop() > hT + hH - wH) {
        jQuery(window).off("scroll", startCounter2);
        jQuery('.love_count2').each(function() {
            var $this = jQuery(this);
            jQuery({
                Counter: 0
            }).animate({
                Counter: $this.text()
            }, {
                duration: 2000,
                easing: 'swing',
                step: function() {
                    $this.text(Math.ceil(this.Counter) + '+');
                }
            });
        });
    }
}

$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });

});

//new WOW().init();

$(".playbtn").click(function() {
    $(".videothumbnails").hide();
    $("#yt")[0].src += "?autoplay=1";
    $("#yt").show();
});

$(document).ready(function() {
    //shared variable
    var max = 0,
        $els = $('.eulH');
    $els.each(function() {
        max = Math.max($(this).height(), max);
    });

    $els.height(max)

    $('.lng_select').on('click', function(e) {
        var hostName = '';
        if (window.location.hostname.search('^([a-z]{2}\\.|www)') === 0) {
            var parts = window.location.hostname.split('.');
            parts.shift();
            hostName = parts.join('.');
        } else {
            hostName = window.location.hostname;
        }
        hostName = $(this).data('lng') + '.' + hostName;
        window.location.href = window.location.href.replace(window.location.hostname, hostName);
    });
});