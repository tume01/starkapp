var ProductFormValidation = function() {
    // Init Bootstrap Forms Validation, for more examples you can check out https://github.com/jzaefferer/jquery-validation
    var initValidationBootstrap = function(){
        jQuery('.js-validation-bootstrap').validate({
            ignore: [],
            //ignore: '',
            errorClass: 'help-block animated fadeInDown',
            errorElement: 'div',
            errorPlacement: function(error, e) {
                console.log('error');
                jQuery(e).parents('.form-group > div').append(error);
            },
            highlight: function(e) {
                var elem = jQuery(e);
                console.log('high');

                elem.closest('.form-group').removeClass('has-error').addClass('has-error');
                elem.closest('.help-block').remove();
            },
            success: function(e) {
                var elem = jQuery(e);
                console.log('clean');

                elem.closest('.form-group').removeClass('has-error');
                elem.closest('.help-block').remove();
            },
            rules: {
                'name': {
                    required: true                    
                },
                'select2Provider': {
                    required: true
                    //email: true
                },
                'price': {
                    required: true                    
                },
                /*'val-confirm-password': {
                    required: true,
                    equalTo: '#val-password'
                },*/
                'actualStock': {
                    required: true
                },
                'minStock' : {
                    required: true
                },
                'selectProductType': {
                    required: true
                }
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un nombre'                    
                },
                'select2Provider': {
                    required: 'Por favor seleccione al menos un proveedor'                    
                },
                'price': {
                    required: 'Por favor ingrese un precio'                    
                },
                'actualStock': {
                    required: 'Por favor ingrese el stock actual'
                },
                'minStock': {
                    required: 'Por favor ingrese un stock mínimo'
                },
                'selectProductType': {
                    required: 'Por favor seleecione un tipo de producto'
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
jQuery(function(){ ProductFormValidation.init(); });
