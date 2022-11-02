$(document).ready(function(){
    $('#crearCapacitacion').validate({
        errorclass: "invalido",
        rules:{
            nombre_empresa:{
                required: true
            },
            nombre:{
                required: true,
                maxlength: 30
            },
            duracion:{
                required: true,
                number: true,
                max: 24
            },
            fecha:{
                required: true
            },
            comuna:{
                required: true
            },
            ubicacion:{
                required: true,
                maxlength: 50
            }
        },
        messages:{
            nombre_empresa:{
                required: "Campo Requerido"
            },
            nombre:{
                required: "Campo Requerido",
                maxlength: "Máximo 30 caracteres"
            },
            duracion:{
                required: "Campo Requerido",
                number: "Solo se aceptan números o decimales",
                max: "Máximo 24 horas"
            },
            fecha:{
                required: "Campo Requerido"
            },
            comuna:{
                required: "Campo Requerido"
            },
            ubicacion:{
                required: "Campo Requerido",
                maxlength: "Máximo 50 caracteres"
            }
        },
        errorPlacement: function(error, element){
            if(element.is("#txbHoras")){
                error.insertAfter('#divHoras')
            }
            else{
                error.insertAfter(element)
            }
        }
    });
});