
$(document).ready(function(){
    desciptions = $('.description');


    for (let index = 0; index < desciptions.length; index++) {
        const description = desciptions[index].innerHTML;
        description_arr = description.split(" ");
        new_des = "";
        for(let i = 0; i < description_arr.length;i++){
            part_des = description_arr[i]
            if (part_des[0] == "#"){
                part_des = part_des.substring(1);
                part_des = "<a href=/search/?q=%23"+part_des+">#"+part_des+"</a>";
                // console.log("test");
            }
            new_des += part_des + " ";

        }
        // console.log(new_des)
        desciptions[index].innerHTML = new_des;
    }
})

