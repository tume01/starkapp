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
                'name': {
                    required: true,
                },
                'description': {
                    required: true,
                },
                'ruc': {
                    minlength: 11,
                    maxlength: 11,
                },
                'environment': {
                    required: true
                },
                'seat': {
                    required: true                  
                },
                'event_type': {
                    required: true
                },
                'start_date' : {
                    required: true
                },
                'end_date' : {
                    required: true
                },
                'user': {
                    required: false
                },
                'assistance': {
                    required: true
                },
                'price_member': {
                    required: true
                },
                'price_invited': {
                    required: true
                },
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese el nombre del evento',
                },
                'description': {
                    required: 'Por favor ingrese la descripción del evento'                    
                },
                'ruc': {
                    minlength: 'El RUC debe tener 11 dígitos',
                    maxlength: 'El RUC debe tener 11 dígitos'
                },
                'environment': {
                    required: 'Por favor ingrese el ambiente donde se realizará el evento'
                },
                'seat': {
                    required: 'Por favor seleccione una sede'
                },
                'event_type': {
                    required: 'Por favor seleccione el tipo de evento'
                },
                'start_date': {
                    required: 'Por favor elija la fecha y hora de inicio del evento',
                },
                'end_date': {
                    required: 'Por favor elija la fecha y hora de fin del evento'
                },
                'assistance': {
                    required: 'Por favor ingrese el número de participantes'
                },
                'price_member': {
                    required: 'Por favor ingrese el precio del evento para los socios'
                },
                'price_invited': {
                    required: 'Por favor ingrese el precio del evento para los invitados'
                },
                'user': {
                    required: 'Por favor coloque el código del usuario'
                } 
            }
        });
    };

    return {
        init: function () {
            // Init Bootstrap Forms Validation
            console.log("entro");
            initValidationBootstrap();

            // Init Validation on Select2 change
            jQuery('.js-select2').on('change', function(){
                jQuery(this).valid();
            });
        }
    };
}();

$(document).ready(function() {
    $('#user').change(function() {
        var user_id = $("#user").val();
        var url = $("#user").data('url');
        var requestData = {
            'document_number' : user_id
        }
        console.log(url);
        $.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : requestData, // data sent with the post request

            // handle a successful response
            success : function(data) {
                if(data)
                {
                    console.log(data);
                    var full_name = data.name + " " + data.lastName + " "+data.secondLastName;
                    $("#user_name").html(full_name);
                }
                else
                {
                    $("#user_name").html("No se encuentra el usuario");
                }

            },
            error : function(xhr,errmsg,err) {
                console.log("ERROR"); // another sanity check
            }
        });
    });
});

// Initialize when page loads
jQuery(function(){ ProviderFormValidation.init(); });