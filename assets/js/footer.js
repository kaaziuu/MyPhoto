$(document).ready(function () {
    var body = document.body,
    html = document.documentElement;

    var height = Math.max( body.scrollHeight, body.offsetHeight, 
        html.clientHeight, html.scrollHeight, html.offsetHeight );
    // console.log(height);
    // console.log(screen.height);

    if(screen.height >= height){
        $('.footer').addClass('fixed-bottom')
    }
})