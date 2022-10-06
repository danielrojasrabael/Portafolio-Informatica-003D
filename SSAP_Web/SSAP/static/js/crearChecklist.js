$(document).ready(function(){
    $("#formCrear").validate({
        errorclass: "invalido",
        rules:{
            item_checklist:{
                required: true,
                maxlength: 30 
            },
        },
        messages:{
            item_checklist:{
                required: "Campo requerido",
                maxlength: "Máximo 30 caracteres"
            }
        },
    });
});