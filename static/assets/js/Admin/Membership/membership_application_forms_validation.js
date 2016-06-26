var MembershipRequestFormValidation = function() {
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
                'firstName': {
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
                    min: 1,  
                    remote: {
                        url: url,
                        type: "post",
                        data: {
                            name: function() {
                                return $( "#num_doc" ).val();
                            }, 'csrfmiddlewaretoken': CSRF_TOKEN,
                        }
                    },
                    maxlength: {
                        depends: function (elem) {
                            if($("#example-select1").val()==1 && ($('#num_doc').val().length == 8)) {
                                return false;
                            }else if($("#example-select1").val()==2 && ($('#num_doc').val().length == 12)){
                                return false;
                            }else{
                                return true;
                            }
                        }
                    },                            
                },
                'gender':{
                    required:true
                },
                'nationality':{
                    required:true,
                    maxlength:20
                },
                'workPlace':{
                    required:true,
                    maxlength:200
                },
                'workPlaceJob':{
                    required:true,
                    maxlength:200   
                },
                'workPlacePhone':{
                    required:true,
                    number:true,
                    minlength:7
                },
                'maritalStatus':{
                    required:true,
                    maxlength:20  
                },
                'cellphoneNumber':{
                    required:true,
                    number:true,
                    minlength:9
                },
                'phone':{
                    required:true,
                    number:true,
                    minlength:7
                },
                'specialization':{
                    required:true,
                    maxlength:200  
                },
                'birthDate' : {
                    required: true
                },
                'birthPlace': {
                    required: true,
                    maxlength:200
                },
                'email': {
                    required: true,
                    maxlength:200
                },
                'comments': {
                    required: true,
                    maxlength:200
                },
                'initialDate' : {
                    required: true
                },
                'finalDate': {
                    required: true
                },
                'address:':{
                    required:true                    
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
                'firstName': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre debe tener máximo 200 caracteres'
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
                    min: 'Por favor ingrese un documento válido' ,
                    remote: 'Este documento ya esta en uso',
                    maxlength: 'Por favor ingrese un documento válido'                    
                },
                'comments': {
                    required: 'Por favor ingrese un comentario',
                    maxlength: 'El comentario debe tener máximo 200 caracteres'
                },
                'initialDate': {
                    required: 'Por favor seleccione una fecha'
                },
                'finalDate': {
                    required: 'Por favor ingrese una dirección'
                },
                'nationality':{
                    required:'Por favor ingrese una nacionalidad',
                    maxlength:'La nacionalidad debe tener máximo 20 caracteres'
                },
                'workPlace':{
                    required:'Por favor ingrese su centro de trabajo',
                    maxlength:'El centro de trabajo debe tener máximo 200 caracteres'
                },
                'workPlaceJob':{
                    required:'Por favor ingrese su puesto de trabajo',
                    maxlength:'El puesto de trabajo debe tener máximo 200 caracteres'
                },
                'workPlacePhone':{
                    required:'Por favor ingrese el teléfono del lugar de trabajo',
                    number: 'Por favor ingrese un número válido',
                    minlength:'El telefono deber tener más de 6 digitos'
                },
                'maritalStatus':{
                    required:'Por favor ingrese un estado civil',
                    maxlength:'El estado civil debe tener máximo 200 caracteres'  
                },
                'cellphoneNumber':{
                    required:'Por favor ingrese un número celular',
                    number: 'Por favor ingrese un número válido',
                    minlength:'El telefono deber tener 9 digitos'
                },
                'phone':{
                    required:'Por favor ingrese un teléfono',
                    number: 'Por favor ingrese un número válido',
                    minlength:'El telefono deber tener más de 6 digitos'
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
                'email': {
                    required: 'Por favor ingrese un mail',
                    maxlength:'El mail debe tener máxmo 200 caracteres'
                },
                'address':{
                    required:'Por favor ingrese una dirección'
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
                'photo':{
                    required: 'Por favor inrese una foto'
                }                
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
jQuery(function(){ MembershipRequestFormValidation.init(); });
