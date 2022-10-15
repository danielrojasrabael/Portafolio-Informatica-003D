$(document).ready(function(){
    $("#visita").validate({
        errorclass: "invalido",
        rules:{
            comuna:{
                required: true
            },
            ubicacion:{
                required: true,
                maxlength: 50
            },
            fecha:{
                required: true
            }
        },
        messages:{
            comuna:{
                required: "Campo requerido"
            },
            ubicacion:{
                required: "Campo requerido",
                maxlength: "Máximo 50 caracteres"
            },
            fecha:{
                required: "Campo requerido"
            }
        }
    });
});