<<<<<<< Updated upstream
=======
localID = 0
>>>>>>> Stashed changes

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

function addComment(id,user) {
    comment = $('#id_comment').val();

    $("#allCom").prepend('<div class="mb-1 comments" id="coml'+localID+'"><b>'+
                            comment+'</b><br><small>'+
                            user+'</small>'+
                            '<img id="adOnClick"  src="/assets/icon/trash-can.png">'+
                            '</div>');

    $("#adOnClick").attr('onclick','deleteCom('+localID+',"'+user+'")');
    $('#adOnClick').removeAttr('id');

    localID++;
    $.ajax
    ({
        url: '.',
        data: {
            'id':id,
            'comment':comment,
            'f':'comment'
        },
        dataType: 'json',
        type: 'POST',




    });

}

function deleteCom(pk,user=null){
    // alert(pk);

    useAuthor = "false";
    // alert(test)
    if (user != null){
        useAuthor = "true";
        $("#coml"+pk).remove();
        if(pk == localID){
            localID--;
        }
        alert(localID)
    }
    else{
        $('#com'+pk).remove()
    }

    $.ajax({
        url: '.',
        data: {
            'id': pk,
            'f': 'deleteComment',
            'useAuthor': useAuthor,
            'author' : user
            },
        dataType: 'json',
        type: 'POST'
    })
}