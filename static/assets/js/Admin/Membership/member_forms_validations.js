var MemberFormValidation = function() {
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
                'paternalLastName': {
                    required: true,
                    maxlength:200
                    //email: true
                },
                'maternalLastName': {
                    required: true,
                    maxlength:200
                    //email: true
                },
                'num_doc': {
                    required: true,    
                    remote: {
                        url: url,
                        type: "post",
                        data: {
                            username: function() {
                                return $( "#num_doc" ).val();
                            }, 'csrfmiddlewaretoken': CSRF_TOKEN, 
                            id_member: function() {
                                return $( "#id" ).val();
                            }
                        }
                    }                           
                },                              
                'address': {
                    required: true,
                    maxlength:200
                },
                'department': {
                     required: true,                             
                },  
                 'province': {
                     required: true,                           
                },  
                 'district': {
                     required: true,                           
                },  
                'phone': {
                    required: true,
                    minlength:7
                    
                },
                'email': {
                    required: true,
                    email: true
                },
                'initialDate': {
                    required: true
                },
                'finalDate':{
                    required:true
                }
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre no puede tener más de 200 caracteres'
                },
                'paternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'maternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'num_doc': {
                    required: 'Por favor ingrese un dni' ,
                    remote: 'Este documento ya esta en uso'                   
                },              
                'address': {
                    required: 'Por favor ingrese una dirección',
                    maxlength: 'La dirección no puede tener más de 200 caracteres'
                },
                'department': {
                     required: "Por favor seleccione un departamento",                             
                },  
                 'province': {
                     required: "Por favor seleccione una provincia",                           
                },  
                 'district': {
                     required: "Por favor seleccione un distrito",                           
                },
                'phone': {
                    required: 'Por favor ingrese un teléfono',   
                    minlength:'El telefono deber tener más de 6 digitos'                 
                },
                
                'email': {
                    required:'Por favor ingrese un email',
                    email:'Por favor ingrese un email válido'                
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
jQuery(function(){ MemberFormValidation.init(); });
