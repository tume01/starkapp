var UserFormValidation = function() {
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
                    maxlength: 200,
                    remote: {
                        url: url,
                        type: "post",
                        data: {
                            name: function() {
                                return $( "#name" ).val();
                            }, 'csrfmiddlewaretoken': CSRF_TOKEN, 
                            user: user
                        }
                    }   
                },
                'password':{
                	required:true,
                	maxlength:200
                }
            },
            messages: {                
                'name': {
                    required: 'Por favor ingrese un nombre de usuario',
                    maxlength: 'El usuario no puede tener más de 200 caracteres',
                    remote: 'Este usuario ya está en uso'
                },
                'password':{
                	required: 'Por favor ingrese una clave',
                	maxlength:'La clave no puede tener más de 200 caracteres'
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
jQuery(function(){ UserFormValidation.init(); });
