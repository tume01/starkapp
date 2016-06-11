var ProviderFormValidation = function() {
    // Init Bootstrap Forms Validation, for more examples you can check out https://github.com/jzaefferer/jquery-validation
    var initValidationBootstrap = function(){
        jQuery('.js-validation-bootstrap').validate({
            ignore: [],
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
                'region': {
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
                'email': {
                    required: true,
                    email: true
                },
                'postal': {
                    required: true,
                    minlength: 5
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
                'region': {
                    required: 'Por favor ingrese una región'                    
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
                'email': 'Por favor ingrese un email válido',
                'postal': {
                    required: 'Por favor ingrese un código postal',
                    minlength: 'El código postal debe tener 5 caracteres'
                },
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

    var LimitCharactersRUC = function () {
    var element = document.getElementById('ruc');
    var limitCharacters = 10;
    $("#ruc").keydown(function (event) {
        // Allow only backspace and delete
        console.log($(this).val().length);
        if($(this).val().length <= limitCharacters || event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 )
        {
            if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9) {
                // let it happen, don't do anything
            } else {
                // Ensure that it is a number and stop the keypress
                if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                    event.preventDefault();
                }
            }
        }else{
            
            event.preventDefault();
        }          
       
    });


    };

    var LimitCharactersPhone = function () {
    var element = document.getElementById('phone');
    var limitCharacters = 10;
    $("#phone").keydown(function (event) {
        // Allow only backspace and delete
        console.log($(this).val().length);
        if($(this).val().length <= limitCharacters || event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 )
        {
            if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9) {
                // let it happen, don't do anything
            } else {
                // Ensure that it is a number and stop the keypress
                if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                    event.preventDefault();
                }
            }
        }else{
            
            event.preventDefault();
        }          
       
    });


    };

    var LimitCharactersContactPhone = function () {
    var element = document.getElementById('contactPhone');
    var limitCharacters = 10;
    $("#contactPhone").keydown(function (event) {
        // Allow only backspace and delete
        console.log($(this).val().length);
        if($(this).val().length <= limitCharacters || event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 )
        {
            if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9) {
                // let it happen, don't do anything
            } else {
                // Ensure that it is a number and stop the keypress
                if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                    event.preventDefault();
                }
            }
        }else{
            
            event.preventDefault();
        }          
       
    });


    };

    return {
        init: function () {
            // Init Bootstrap Forms Validation
            initValidationBootstrap();
            LimitCharactersRUC();
            LimitCharactersPhone();
            LimitCharactersContactPhone();
            // Init Validation on Select2 change
            jQuery('.js-select2').on('change', function(){
                jQuery(this).valid();
            });
        }
    };
}();

// Initialize when page loads
jQuery(function(){ ProviderFormValidation.init(); });

