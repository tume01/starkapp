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
                'ruc': {
                    required: true,
                    minlength: 11
                },
                'businessName': {
                    required: true
                    //email: true
                },
                'province': {
                    required: true                    
                },
                /*'val-confirm-password': {
                    required: true,
                    equalTo: '#val-password'
                },*/
                'distric': {
                    required: true
                },
                'registrationDate' : {
                    required: true
                },
                'address': {
                    required: true
                },
                'phone': {
                    required: true,
                    minlength: 7
                },
                'effectiveTime': {
                    required: true
                },
                'email': {
                    required: true,
                    email: true
                },
                'contactName': {
                    required: true
                },
                'contactPhone': {
                    required: true,
                    minlength: 7
                }
            },
            messages: {
                'ruc': {
                    required: 'Por favor ingrese un RUC',
                    minlength: 'El RUC debe tener 11 caracteres'
                },
                'businessName': {
                    required: 'Por favor ingrese una razón social'                    
                },
                'province': {
                    required: 'Por favor ingrese una provincia'                    
                },
                'distric': {
                    required: 'Por favor ingrese un distrito'
                },
                'registrationDate': {
                    required: 'Por favor seleccione una fecha'
                },
                'address': {
                    required: 'Por favor ingrese una dirección'
                },
                'phone': {
                    required: 'Por favor ingrese un teléfono',
                    minlength: 'El teléfono debe tener mínimo 7 caracteres'
                },
                'effectiveTime': {
                    required: 'Por favor ingrese tiempo de vigencia'
                },
                'email': 'Por favor ingrese un email válido',
                'contactName': {
                    required: 'Por favor ingrese un nombre de contacto'
                },
                'contactPhone': {
                    required: 'Por favor ingrese un teléfono de contacto',
                    minlength: 'El teléfono de contacto debe tener mínimo 7 caracteres'
                }
                /*
                'val-confirm-password': {
                    required: 'Please provide a password',
                    minlength: 'Your password must be at least 5 characters long',
                    equalTo: 'Please enter the same password as above'
                },*/

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
