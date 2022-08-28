$(document).ready(function(){
    jQuery.validator.addMethod("rut", function(value, element) {
        return this.optional(element) || /^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$/i.test(value);
    }, "Rut Inválido");
});