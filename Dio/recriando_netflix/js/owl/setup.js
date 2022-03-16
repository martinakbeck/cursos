$('.owl-carousel').owlCarousel({
    loop:true, /*se quer fazer o efeito de loop*/
    margin:10, /*distancia entre uma imagem e outra*/
    nav:false, /*nagegação*/
    responsive:{
        0:{
            items:1
        },
        600:{
            items:4
        },
        1000:{
            items:7
        }
    }
})