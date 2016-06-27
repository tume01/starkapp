var AffiliateFormValidation = function() {
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
                },
                'maternalLastName': {
                    required: true,
                    maxlength:200
                },
                'num_doc': {
                    required: true,   
                    number: true, 
                    remote: {
                        url: url,
                        type: "post",
                        data: {
                            num_doc: function() {
                                return $( "#num_doc" ).val();
                            }, 'csrfmiddlewaretoken': CSRF_TOKEN, 
                            id_member: function() {
                                return $( "#id_member" ).val();
                            }
                        }
                    },
                    maxlength: {
                        depends: function (elem) {
                            if($("#example-select").val()==1 && ($('#num_doc').val().length == 8)) {
                                return false;
                            }else if($("#example-select").val()==2 && ($('#num_doc').val().length == 12)){
                                return false;
                            }else{
                                return true;
                            }
                        }
                    }, 
                    min: 1                       
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
                    number: true, 
                    minlength:7,
                    min:1
                    
                },
                'email': {
                    required: true,
                    email: true
                },                
                'gender':{
                    required:true
                },
                'nationality':{
                    required:true,
                    maxlength:20
                },
                'maritalStatus':{
                    required:true,
                    maxlength:20  
                },                
                'specialization':{
                    required:true,
                    maxlength:200  
                },
                'birthDate' : {
                    required: true,
                    domain: true
                },
                'birthPlace': {
                    required: true,
                    maxlength:200
                },                                                                
                'birthDepartment':{
                    required:true
                },
                'birthProvince':{
                    required:true
                },
                'birthDistrict':{
                    required:true
                },
                'photo':{
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
                    required: 'Por favor ingrese un número de documento' ,
                    number: 'Por favor ingrese un documento válido' ,
                    remote: 'Este documento ya esta en uso',
                    min: 'Por favor ingrese un documento válido' ,    
                    maxlength: 'Por favor ingrese un documento válido'             
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
                    number: 'Por favor ingrese un número válido' ,
                    minlength:'El telefono deber tener más de 6 digitos',
                    min: 'Por favor ingrese un telefono válido'                  
                },
                
                'email': {
                    required:'Por favor ingrese un email',
                    email:'Por favor ingrese un email válido'                
                },
                'birthDepartment':{
                    required:'Por favor ingrese un departamento'
                },
                'birthProvince':{
                    required:'Por favor ingrese una provincia'
                },
                'birthDistrict':{
                    required:'Por favor ingrese un distrito'
                },
                'specialization':{
                    required:'Por favor ingrese una especialización',
                    maxlength:'La especialización debe tener máximo 200 caracteres'  
                },
                'birthDate' : {
                    required: 'Por favor ingrese la fecha de nacimiento'
                },
                'birthPlace': {
                    required: 'Por favor ingrese un lugar de nacimiento',
                    maxlength:'El lugar de nacimiento debe tener máximo 200 caracteres'
                },
                'nationality':{
                    required:'Por favor ingrese una nacionalidad',
                    maxlength:'La nacionalidad debe tener máximo 20 caracteres'
                },
                'maritalStatus':{
                    required:'Por favor ingrese un estado civil',
                    maxlength:'El estado civil debe tener máximo 200 caracteres'  
                },
                'photo':{
                    required: 'Por favor inrese una foto'
                }                
            }
        });
    };

    jQuery.validator.addMethod("domain", function(value, element) {
        var today=new Date();
    var sbirthDate = $('#birthDate').val();
    var splitdate = sbirthDate.split("/");
    var birthDate = new Date(splitdate[1]+" "+splitdate[0]+" "+splitdate[2]);
    if(birthDate >= today){ return false;}
    else {return true;}
    }, "La fecha no puede ser mayor a la de hoy");

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
jQuery(function(){ AffiliateFormValidation.init(); });
