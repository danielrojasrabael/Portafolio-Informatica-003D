function cambioTipo(){
    if($("#tipo option:selected").val()=="ASESORÍA"){
        $("#tipo-asesoria-div").show();
    } 
    else{
        $("#tipo-asesoria-div").hide();
    }
}

$(document).ready(function(){
    cambioTipo();

    $("#formCrear").validate({
        errorclass: "invalido",
        rules:{
            tipo:{
                reqired: true
            },
            tipo_asesoria:{
                required: true
            },
            motivo:{
                required: true,
                maxlength: 300
            }
        },
        messages:{
            tipo:{
                reqired: "Campo Requerido"
            },
            tipo_asesoria:{
                required: "Campo Requerido"
            },
            motivo:{
                required: "Campo Requerido",
                maxlength: "Máximo 300 caracteres"
            }
        }
    });
});