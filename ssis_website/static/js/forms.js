$(document).ready(function(){
    $("#gender_otr").click(function(){
        $("#gender_other_add").prop("disabled", false);
    });

    $(".gender").click(function(){
        $("#gender_other_add").prop("disabled", true);
    });

    $("#flash_message").delay(3000).slideUp(400);
})