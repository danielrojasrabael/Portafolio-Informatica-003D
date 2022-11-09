$(document).ready(function(){
    jQuery.validator.addMethod("rut", function(value, element) {
        return this.optional(element) || /^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$/i.test(value);
    }, "Rut Inválido");

    jQuery.validator.addMethod("telefono", function(value, element) {
        return this.optional(element) || /^([+]\d{3}).*(\d{4}).*(\d{4})+$/i.test(value);
    }, "Teléfono Inválido");

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

    $('.btn-close').click(function(){
        $('.alert').slideUp(500)
    });
});