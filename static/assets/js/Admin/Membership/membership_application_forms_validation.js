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
                'lastName': {
                    required: true,
                    maxlength:200
                    //email: true
                },
                'dni': {
                    required: true                    
                },
                /*'val-confirm-password': {
                    required: true,
                    equalTo: '#val-password'
                },*/
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
                'lastName': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'dni': {
                    required: 'Por favor ingrese un dni'                    
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
