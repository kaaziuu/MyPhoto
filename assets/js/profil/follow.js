$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function follow(nick,userPage=true){
    id = "#follow";
    if(!userPage){
        id += nick
    }
    $(id).removeClass('btn-primary').addClass('btn-secondary');
    $(id).removeAttr('onclick');
    $(id).attr('onclick', 'unfollow("'+nick+ '")');
    $(id).text('unfollow');
    fl = $('#followers').html();
    // alert(fl);
    fl = parseInt(fl);
    fl++;
    $('#followers').text(" "+fl);
    redirect = '.'
    if(userPage){
        redirect = '/u/' + nick;
    }

    $.ajax
    ({
        url: redirect,
        cache: false,
        data: {
            'nick': nick,
            'f' : 'follow'
        },
        dataType: 'json',
        type: 'POST',



    });

}

function unfollow(nick, userPage = true){
    id = "#follow";
    if (!userPage) {
        id += nick
    }
    $(id).removeClass('btn-secondary').addClass('btn-primary');
    $(id).removeAttr('onclick');
    $(id).attr('onclick', 'follow("'+nick+ '")');
    $(id).text('follow');
    fl = $('#followers').html();
    // alert(fl);
    fl = parseInt(fl);
    fl--;
    $('#followers').text(" "+fl);
    redirect = '/search/'
    if (userPage) {
        redirect = '/u/' + nick;
    }

    $.ajax
    ({
        url:redirect,
        cache: false,
        data: {
            'nick': nick,
            'f' : 'unfollow'
        },
        dataType: 'json',
        type: 'POST',


//        success: function(data){
//            console.log(data)
//        }

    });
}