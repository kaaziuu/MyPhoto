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

function follow(nick){
    $("#follow").removeClass('fl-btn').addClass('ufl-btn');
    $('#follow').removeAttr('onclick');
    $('#follow').attr('onclick', 'unfollow("'+nick+ '")');
    $('#follow').text('unfollow');
    fl = $('#followers').html();
    // alert(fl);
    fl = parseInt(fl);
    fl++;
    $('#followers').text(" "+fl);


    $.ajax
    ({
        url:'/u/'+nick,
        cache: false,
        data: {
            'nick': nick,
            'f' : 'follow'
        },
        dataType: 'json',
        type: 'POST',



    });

}

function unfollow(nick){
    $("#follow").removeClass('ufl-btn').addClass('fl-btn');
    $('#follow').removeAttr('onclick');
    $('#follow').attr('onclick', 'follow("'+nick+ '")');
    $('#follow').text('follow');
    fl = $('#followers').html();
    // alert(fl);
    fl = parseInt(fl);
    fl--;
    $('#followers').text(" "+fl);


    $.ajax
    ({
        url:'/u/'+nick,
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