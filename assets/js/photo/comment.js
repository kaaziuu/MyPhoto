
localID = 0;
var deleteIndex = [];


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
    localID++;
    comment = $('#id_comment').val();
    $('#id_comment').focus(function(){$(this).val('')});

    $("#allCom").prepend('<div class="mb-1 comments" id="coml'+localID+'"><b>'+
                            comment+'</b><br><small>'+
                            user+'</small>'+
                            '<img id="adOnClick"  src="/assets/icon/trash-can.png">'+
                            '</div>');

    $("#adOnClick").attr('onclick','deleteCom('+localID+','+id+',"'+user+'")');
    $('#adOnClick').removeAttr('id');


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

function deleteCom(pk,idPhoto=null,user=null){
    // alert(pk);

    useAuthor = "false";
    // alert(test)
    if (user != null){
        useAuthor = "true";
        $("#coml"+pk).remove();
        pk = parseInt(pk);
        pk = localID - pk;
        tpk = pk
        deleteIndex.forEach(function(item){
            if(pk>item){
                pk --;
            }
        });
        deleteIndex.push(tpk);

        console.log(pk)
    }
    else{
        $('#com'+pk).remove();
        idPhoto = 'nic';
    }

    $.ajax({
        url: '.',
        data: {
            'id': pk,
            'f': 'deleteComment',
            'useAuthor': useAuthor,
            'author' : user,
            'photoID': idPhoto
            },
        dataType: 'json',
        type: 'POST'
    });
}