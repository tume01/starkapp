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
                'card_number' : {
                    required: true,
                    number:true,
                    maxlength: 11,
                },
                'csv': {
                    required: true,
                    number:true,
                    maxlength: 3,
                },
                'card_holder': {
                    required: true,
                },
                'name_social':{
                  required: function (element) {
                    console.log('ola');
                    console.log($("#payment").val());
                     if($("#payment:checked").val() == 'invoice'){
                         return true;                
                     }
                     else
                     {
                         return false;
                     }  
                  } 
                },
                'ruc':{
                  required: function (element) {
                     if($("#payment:checked").val() == 'invoice'){
                         return true;                
                     }
                     else
                     {
                         return false;
                     }  
                  }  
                },
                'address':{
                  required: function (element) {
                     if($("#payment:checked").val() == 'invoice'){
                         return true;                
                     }
                     else
                     {
                         return false;
                     }  
                  }
                },
            },
            messages: {
                'card_number': {
                    required: 'Campo Requerido',
                    maxlength: 'Por favor ingrese maximo 16 caracteres',
                    number: 'Por favor ingrese solo números'
                },
                'csv': {
                    required: 'Campo Requerido',
                    maxlength: 'Por favor ingrese maximo 3 caracteres',
                    number: 'Por favor ingrese solo números'
                },
                'card_holder': {
                    required: 'Campo Requerido'
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
