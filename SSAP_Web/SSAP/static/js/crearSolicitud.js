function cambioTipo(){
    if($("#tipo option:selected").val()=="ASESORÍA"){
        $("#tipo-asesoria-div").show();
    } 
    else{
        $("#tipo-asesoria-div").hide();
    }
}

$(document).ready(function(){
    $("#formCrear").validate({
        errorclass: "invalido",
        rules:{
            motivo:{
                required: true,
                maxlength: 1000
            }
        },
        messages:{
            motivo:{
                required: "Campo Requerido",
                maxlength: "Máximo 1000 caracteres"
            }
        }
    });
});