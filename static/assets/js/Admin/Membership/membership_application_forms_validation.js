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
                'firstName': {
                    required: true,
                    maxlength: 200
                },
                'paternalLastName': {
                    required: true,
                    maxlength:200
                },
                'maternalLastName': {
                    required: true,
                    maxlength:200
                },
                'num_doc': {
                    required: true,    
                    remote: {
                        url: url,
                        type: "post",
                        data: {
                            username: function() {
                                return $( "#num_doc" ).val();
                            }, 'csrfmiddlewaretoken': CSRF_TOKEN
                        }
                    }                           
                },
                'comments': {
                    required: true,
                    maxlength:200
                },
                'initialDate' : {
                    required: true
                },
                'finalDate': {
                    required: true
                }
            },
            messages: {
                'firstName': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre debe tener máximo 200 caracteres'
                },
                'paternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'maternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'num_doc': {
                    required: 'Por favor ingrese un dni' ,
                    remote: 'Este documento ya esta en uso'                   
                },
                'comments': {
                    required: 'Por favor ingrese un comentario',
                    maxlength: 'El comentario debe tener máximo 200 caracteres'
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
