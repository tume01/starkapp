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
                    minlength: 11
                },
                'attendance': {
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
                'start_date': {
                    required: true
                },
                'end_date' : {
                    required: true
                },
                'activity_type': {
                    required: true
                },
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un Nombre',
                },
                'attendance': {
                    required: 'Por favor ingrese una capacidad'
                },
                'price': {
                    required: 'Por favor ingrese un precio'
                },
                'start_date': {
                    required: 'Por favor ingrese una fecha de inicio'
                },
                'end_date': {
                    required: 'Por favor ingrese una fecha fin'
                },
                'activity_type': {
                    required: 'Por favor seleccione un tipo de actividad'
                },
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
