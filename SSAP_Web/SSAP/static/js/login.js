$(document).ready(function(){
    $("#formLogin").validate({
        errorclass: "invalido",
        rules:{
            rut:{
                required: true,
                rut: true,
                minlength: 12,
                maxlength: 12
            },
            password:{
                required: true,
                minlength: 4
            },
        },
        messages:{
            rut:{
                required: "Campo Requerido",
                minlength: "12 carácteres necesarios",
                maxlength: "12 carácteres necesarios"
            },
            password:{
                required: "Campo Requerido",
                minlength: "4 carácteres mínimo"
            }
        }
    })  
});