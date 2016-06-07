var MembershipTypeFormValidation = function() {
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
                    maxlength: 200
                },
                'guests':{
                	required:true,
                    number: true,
                    min: 1                
                },
                'price':{
                    required:true,
                    number: true,
                    min: 1
                },
                'billing':{
                    required:true,
                    maxlength:200
                }
            },
            messages: {                
                'name': {
                    required: 'Por favor ingrese una descripcion',
                    maxlength: 'El usuario no puede tener más de 200 caracteres'
                },
                'guests':{
                	required: 'Por favor ingrese el número de invitados',
                    number: 'Por favor ingrese un número válido',
                    min: 'Por favor ingrese un número válido'               	
                },
                'price':{
                    required:'Por favor ingrese un precio',   
                    number: 'Por favor ingrese un precio válido',
                    min: 'Por favor ingrese un número válido'                
                },
                'billing':{
                    required:'Por favor ingrese el tipo de cobro',
                    maxlength:'El tipo de cobro no puede tener más de 200 caracteres'
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
jQuery(function(){ MembershipTypeFormValidation.init(); });
