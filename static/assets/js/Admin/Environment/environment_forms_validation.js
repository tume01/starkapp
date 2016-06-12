var EnvironmentFormValidation = function() {
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
                'name': {
                    required: true
                },
                'capacity': {
                    required: true
                },
                'description': {
                    required: true
                }
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese el nombre'
                },
                'capacity': {
                    required: 'Por favor ingrese el aforo'
                },
                'description': {
                    required: 'Por favor ingrese una descripción'                    
                }
            }
        });
    };

    var LimitCharactersCapacity = function () {
    var element = document.getElementById('capacity');
    var limitCharacters = 10;
    $("#capacity").keydown(function (event) {
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
            LimitCharactersCapacity();
            // Init Validation on Select2 change
            jQuery('.js-select2').on('change', function(){
                jQuery(this).valid();
            });
        }
    };
}();

// Initialize when page loads
jQuery(function(){ EnvironmentFormValidation.init(); });

