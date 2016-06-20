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
                'name': {
                    required: true,
                    maxlength: 40,
                    minlength: 4
                },
                'description': {
                    required: true,
                    maxlength: 40
                },
                'location': {
                    required: true,
                    maxlength: 40,
                    minlength: 4
                },
                'department': {
                    required: true,
                    notEqualTo: 'Seleccione'
                },
                'province': {
                    required: true,
                    notEqualTo: 'Seleccione'
                },
                'district': {
                    required: true,
                    notEqualTo: 'Seleccione'
                }
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un Nombre',
                    maxlength: 'Por favor ingrese maximo 40 caracteres',
                    minlength: 'Por favor ingrese un nombre de al menos 4 caracteres'
                },
                'description': {
                    required: 'Por favor ingrese una descripcion',
                    maxlength: 'Por favor ingrese maximo 40 caracteres',
                },
                'location': {
                    required: 'Por favor ingrese una direccion',
                    maxlength: 'Por favor ingrese maximo 40 caracteres',
                    minlength: 'Por favor ingrese una direccion de al menos 4 caracteres'
                },
                'department': {
                    required: 'Por favor seleccione un departamento',
                    notEqualTo: 'Por favor seleccione un departamento'
                },
                'province': {
                    required: 'Por favor seleccione una provincia',
                    notEqualTo: 'Por favor seleccione un provincia'
                },
                'district': {
                    required: 'Por favor seleccione un distrito',
                    notEqualTo: 'Por favor seleccione un distrito'
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
