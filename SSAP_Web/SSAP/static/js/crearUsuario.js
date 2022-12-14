//Funcion: Control de formulario según tipo de usuario en creación
function cambioTipo(){
    if($("#tipo option:selected").val()=="CLIENTE"){
        $("#cliente").show()
        $("#profesional").hide()
        $("#administrador").hide()
    } 
    if($("#tipo option:selected").val()=="PROFESIONAL"){
        $("#cliente").hide()
        $("#profesional").show()
        $("#administrador").hide()
    } 
    if($("#tipo option:selected").val()=="ADMINISTRADOR"){
        $("#cliente").hide()
        $("#profesional").hide()
        $("#administrador").show()
    }
}

$(document).ready(function(){
    cambioTipo();

    $("#formCrear").validate({
        errorclass: "invalido",
        rules:{
            username:{
                required: true,
                rut: true,
                minlength: 12,
                maxlength: 12
            },
            password1:{
                required: true,
                minlength: 4
            },
            password2:{
                required: true,
                minlength: 4,
                equalTo: "#id_password1",
            },
            email:{
                required: true,
                maxlength: 150,
                email: true
            },
            comuna:{
                required: true
            },
            direccion:{
                required: true,
                maxlength: 50
            },
            tipo:{
                required: true
            },
            nombre_empresa:{
                required: true
            },
            rubro:{
                required: true
            },
            cant_trabajadores:{
                required: true,
                digits: true
            },
            nombre_profesional:{
                required: true
            },
            nombre_administrador:{
                required: true
            },
            costo_base:{
                required: true,
                digits: true
            },
            fecha_firma:{
                required: true
            },
            profesionalCliente:{
                required: true
            }
        },
        messages:{
            username:{
                required: "Campo Requerido",
                minlength: "12 carácteres necesarios",
                maxlength: "12 carácteres necesarios"
            },
            password1:{
                required: "Campo Requerido",
                minlength: "4 carácteres mínimo"
            },
            password2:{
                required: "Campo Requerido",
                minlength: "4 carácteres mínimo",
                equalTo: "Ambas contraseñas deben ser iguales",
            },
            email:{
                required: "Campo Requerido",
                maxlength: "Máximo 150 carácteres",
                email: "Ingrese un mail válido"
            },
            comuna:{
                required: "Campo Requerido"
            },
            direccion:{
                required: "Campo Requerido",
                maxlength: "Máximo 50 caracteres"
            },
            tipo:{
                required: "Campo Requerido"
            },
            nombre_empresa:{
                required: "Campo Requerido"
            },
            rubro:{
                required: "Campo Requerido"
            },
            cant_trabajadores:{
                required: "Campo Requerido",
                digits: "Solo Números"
            },
            nombre_profesional:{
                required: "Campo Requerido"
            },
            nombre_administrador:{
                required: "Campo Requerido"
            },
            costo_base:{
                required: "Campo Requerido",
                digits: "Solo numeros"
            },
            fecha_firma:{
                required: "Campo Requerido"
            },
            profesionalCliente:{
                required: "Campo Requerido"
            }
        }
    });
});