$(document).ready(function(){
    $("#responderAccidente").validate({
        errorclass: "invalido",
        rules:{
            respuesta_accidente:{
                required: true,
                maxlength: 1000
            }
        },
        messages:{
            respuesta_accidente:{
                required: "Campo Requerido",
                maxlength: "Máximo 1000 caracteres"
            }
        }
    });
});