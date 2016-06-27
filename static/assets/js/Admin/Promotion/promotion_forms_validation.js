var PromotionFormValidation = function() {
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
                'description': {
                    required: true,
                    maxlength: 200
                },
                'percentage':{
                	required:true,
                    number: true,
                    min: 1
                	
                }
            },
            messages: {                
                'description': {
                    required: 'Por favor ingrese una descripción',
                    maxlength: 'La descripción no puede tener más de 200 caracteres'
                },
                'percentage':{
                	required: 'Por favor ingrese un porcentaje',
                    number: 'Por favor ingrese un número válido',
                    min: 'Por favor ingrese un número positivo'
                	
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
jQuery(function(){ PromotionFormValidation.init(); });
