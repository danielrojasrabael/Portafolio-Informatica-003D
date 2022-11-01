$(document).ready(function(){
    $("#formContacto").validate({
        errorclass: "invalido",
        rules:{
            nombre:{
                required: true,
                maxlength: 30
            },
            correo:{
                required: true,
                email: true,
                maxlength: 100
            },
            telefono:{
                required: true,
                maxlength: 30,
                telefono: true
            },
            mensaje:{
                required: true,
                maxlength: 1000
            }
        },
        messages:{
            nombre:{
                required: "Campo requerido",
                maxlength: "Máximo 30 carácteres"
            },
            correo:{
                required: "Campo requerido",
                email: "Email inválido",
                maxlength: "Máximo 100 carácteres"
            },
            telefono:{
                required: "Campo requerido",
                maxlength: "Máximo 30 carácteres"
            },
            mensaje:{
                required: "Campo requerido",
                maxlength: "Máximo 1000 carácteres"
            }
        }
    });
});