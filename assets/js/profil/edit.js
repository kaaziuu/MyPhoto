function show(id){
    qid = '#'+id;
    if($(qid).hasClass('none')){
        $(qid).removeClass('none');
    }
    else{
        $(qid).addClass('none')
    }

}