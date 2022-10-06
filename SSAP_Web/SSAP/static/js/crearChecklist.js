$(document).ready(function(){
    $(".crearItem").validate({
        errorclass: "invalido",
        rules:{
            item:{
                required: true,
                maxlength: 30
            }
        },
        messages:{
            item:{
                required: "Campo requerido",
                maxlength: "Máximo 30 caracteres"
            }
        }
    });
});