var SuspensionFormValidation = function() {
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
                'reason': {
                    required: true,
                    maxlength: 200
                },
                'initialDate': {
                    required: true
                },
                'finalDate':{
                    required:true
                }
            },
            messages: {
                'reason': {
                    required: 'Por favor ingrese un comentario',
                    maxlength: 'El comentario no puede tener más de 200 caracteres'
                },
                'initialDate': {
                    required: 'Por favor ingrese una fecha inicial'
                },
                'finalDate':{
                    required: 'Por favor ingrese una fech final'
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
jQuery(function(){ SuspensionFormValidation.init(); });