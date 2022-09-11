$(document).ready(function(){
    jQuery.validator.addMethod("rut", function(value, element) {
        return this.optional(element) || /^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$/i.test(value);
    }, "Rut Inválido");

    $('.buscarTabla').keyup(function(){
        var buscarTabla = $.trim($(this).val().toUpperCase());
        $("table tr").show().each(function(index){
            if(index !== 0){
                var textoTabla = $.trim($(this).find("th").text().toUpperCase());
                if(textoTabla.indexOf(buscarTabla) === -1){
                    $(this).hide();
                }
            }
        });
    });

    $('#sidebar button').mouseover(function(){
        $(this).css("background-color", "rgb(25, 167, 185)");
        $(this).css("color", "white");
    }).mouseout(function(){
        $(this).css("background-color", "white");
        $(this).css("color", "black");
    });
});