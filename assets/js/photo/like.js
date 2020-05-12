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


function unlike(id,pk) {
    id_q = '#'+id;


    $(id_q).removeClass('like').addClass('unlike');
    $(id_q).removeAttr('onclick');
    $(id_q).attr('onclick', 'like(' + id + ',' + pk +')');

    val = $('#like' + id).html();
    val = parseInt(val)
    val--;
    $('#like' + id).text(val);


    $.ajax
    ({
        url:'.',
        cache: false,
        data: {
            'id': pk,
            'f' : 'like'
        },
        dataType: 'json',
        type: 'POST',




    });

}
function like(id,pk) {

    id_q = '#'+id;
    $(id_q).removeClass('unlike').addClass('like');
    $(id_q).removeAttr('onclick');
    $(id_q).attr('onclick', 'unlike(' + id +','+ pk +')');

    val =  $('#like'+id).html();
    val = parseInt(val)
    val++;
    $('#like' + id).text(val);


    $.ajax
        ({
            url: '.',
            cache: false,
            data: {
                'id': pk,
                'f': 'like'
            },
            dataType: 'json',
            type: 'POST',



        });
}
function deletePhoto(pk){
    console.log("test");
    $.ajax
        ({
        url: '.',
        cache: false,
        data: {
            'id': pk,
            'f': 'DELETE'
        },
        dataType: "json",
        type: "POST",
        success: function(data){
            console.log("test__ater");
        }
    });
    window.location.replace('/');
}

function changeDes(pk){
    const des = $('#editDes'+pk).text();
    $('#editDes'+pk).html(
        '<input id="newDes'+pk+'" type="text" value="'+
        des+
        '"/><button onclick="acceptChange('+
        pk+
        ')"> accept </button>'
    );
}
function acceptChange(pk){
    const newDes = $('#newDes'+pk).val();
    console.log(newDes);
    $("#editDes"+pk).html(newDes);
    $.ajax({
        url: '.',
        data: {
            'id': pk,
            'newDes': newDes,
            'f': "newDes"
        },
        dataType: "json",
        type: "post"
    });
}