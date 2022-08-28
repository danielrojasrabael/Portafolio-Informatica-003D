//Funcion: Control de formulario según tipo de usuario en creación
function cambioTipo(){
    if($("#tipo option:selected").text()=="CLIENTE"){
        $("#cliente").show()
        $("#profesional").hide()
        $("#administrador").hide()
    } 
    if($("#tipo option:selected").text()=="PROFESIONAL"){
        $("#cliente").hide()
        $("#profesional").show()
        $("#administrador").hide()
    } 
    if($("#tipo option:selected").text()=="ADMINISTRADOR"){
        $("#cliente").hide()
        $("#profesional").hide()
        $("#administrador").show()
    }
}

$(document).ready(function(){
    $("#cliente").show()
    $("#profesional").hide()
    $("#administrador").hide()
});