var ProviderFormValidation = function() {
    // Init Bootstrap Forms Validation, for more examples you can check out https://github.com/jzaefferer/jquery-validation
    var initValidationBootstrap = function(){
        jQuery('.js-validation-bootstrap').validate({
            ignore: ['cancel'],
            errorClass: 'help-block animated fadeInDown',
            errorElement: 'div',
            errorPlacement: function(error, e) {
                jQuery(e).parents('.form-group > div').append(error);
            },
            highlight: function(e) {
                var elem = jQuery(e);

                elem.closest('.form-group').removeClass('has-error').addClass('has-error');
                elem.closest('.help-block').remove();
            },
            success: function(e) {
                var elem = jQuery(e);

                elem.closest('.form-group').removeClass('has-error');
                elem.closest('.help-block').remove();
            },
            rules: {
                'names': {
                    required: true,
                    maxlength: 200
                },
                'surnames': {
                    required: true,
                    maxlength:200
                },
                'dni': {
                    required: true,
                    number: true, 
                    min: 1                   
                },
                'document_number': {
                    required: true,
                    number: true, 
                    min: 1                   
                },
                'document_number_entry': {
                    required: true,
                    number: true, 
                    min: 1                   
                },
                'initialDate' : {
                    required: true
                },
                'finalDate': {
                    required: true
                }
            },
            messages: {
                'names': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre debe tener máximo 200 caracteres'
                },
                'surnames': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'dni': {
                    required: 'Por favor ingrese un número de documento' ,
                    number: 'Por favor ingrese un documento válido' ,
                    min: 'Por favor ingrese un documento válido'               
                },
                'document_number': {
                    required: 'Por favor ingrese un número de documento' ,
                    number: 'Por favor ingrese un documento válido' ,
                    min: 'Por favor ingrese un documento válido'               
                },
                'document_number_entry': {
                    required: 'Por favor ingrese un número de documento' ,
                    number: 'Por favor ingrese un documento válido' ,
                    min: 'Por favor ingrese un documento válido'               
                },
                'initialDate': {
                    required: 'Por favor seleccione una fecha'
                },
                'finalDate': {
                    required: 'Por favor ingrese una dirección'
                }
            }
        });


    };

    return {
        init: function () {
            // Init Bootstrap Forms Validation
            initValidationBootstrap();

            // Init Validation on Select2 change
            jQuery('.js-select2').on('change', function(){
                jQuery(this).valid();
            });
        }
    };
}();

// Initialize when page loads
jQuery(function(){ ProviderFormValidation.init(); });
