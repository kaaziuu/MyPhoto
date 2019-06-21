$(document).ready(function () {
    if(screen.width >= 768){
        // alert("Test");
        photos = $('.photos');
        // console.log(photos.length)
        for (let i = 0; i < photos.length; i++){
            // console.log("test");
            const inner  = photos[i].innerHTML;
            // console.log(inner);
            photos[i].remove()
            id = i+1
            $('#inner'+id).html(inner);
            $('#inner'+id).addClass("photos");

        }
    }
})