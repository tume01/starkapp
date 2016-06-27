$( document ).ready(function() {
	console.log( "provider ready!" );
	console.log( "finish provider ready!" );    
});

$('#EditProvider').click(function(){
	console.log('guardar edit provider');

	var ruc = $('#ruc').val();
	var businessName = $('#businessName').val();
	var registrationDate = $('#registrationDate').val();
	var region = $('#region').val();
	var province = $('#province').val();
	var distric = $('#distric').val();
	var address = $('#address').val();
	var phone = $('#phone').val();
	var postal = $('#postal').val();
	var contactName = $('#contactName').val();
	var contactPhone = $('#contactPhone').val();


	if(ruc == '' || businessName == '' ||
	   registrationDate == '' || region == '' || province == '' || distric == '' ||
	   address == '' || phone == '' || postal == '' || contactName == '' ||
	   contactPhone == ''){

		$('#formEditProvider').submit();
	}
	else{
		swal({
	                title: "Editar Proveedor/Concesionario",
	                text: "Se actualizaran los campos alterados. ¿Desea continuar?",
	                type: "info",
	                showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	        },
	        function(){
	        	swal({
	                title: "Proveedor/Concesionario actualizado!",
	                text: "",
	                type: "success",
	                //showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                //cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	            },
	            function(){
	            	$('#formEditProvider').submit();
	            });

	        });

	}
});


$('#NewProvider').click(function(){
	console.log('guardar new provider');

	var ruc = $('#ruc').val();
	var businessName = $('#businessName').val();
	var registrationDate = $('#registrationDate').val();
	var region = $('#region').val();
	var province = $('#province').val();
	var distric = $('#distric').val();
	var address = $('#address').val();
	var phone = $('#phone').val();
	var postal = $('#postal').val();
	var contactName = $('#contactName').val();
	var contactPhone = $('#contactPhone').val();


	if(ruc == '' || businessName == '' ||
	   registrationDate == '' || region == '' || province == '' || distric == '' ||
	   address == '' || phone == '' || postal == '' || contactName == '' ||
	   contactPhone == ''){

		$('#formNewProvider').submit();
	}
	else{
		swal({
	                title: "Crear Proveedor",
	                text: "Se procedera a crear este proveedor. ¿Desea continuar?",
	                type: "info",
	                showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	        },
	        function(){
	        	swal({
	                title: "Proveedor creado!",
	                text: "",
	                type: "success",
	                //showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                //cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	            },
	            function(){
	            	$('#formNewProvider').submit();
	            });

	        });

	}

});


$('#NewConcesionary').click(function(){
	console.log('guardar new provider');

	var ruc = $('#ruc').val();
	var businessName = $('#businessName').val();
	var registrationDate = $('#registrationDate').val();
	var region = $('#region').val();
	var province = $('#province').val();
	var distric = $('#distric').val();
	var address = $('#address').val();
	var phone = $('#phone').val();
	var postal = $('#postal').val();
	var contactName = $('#contactName').val();
	var contactPhone = $('#contactPhone').val();


	if(ruc == '' || businessName == '' ||
	   registrationDate == '' || region == '' || province == '' || distric == '' ||
	   address == '' || phone == '' || postal == '' || contactName == '' ||
	   contactPhone == ''){

		$('#formNewConcesionary').submit();
	}
	else{
		swal({
	                title: "Crear Concesionario",
	                text: "Se procedera a crear este concesionario. ¿Desea continuar?",
	                type: "info",
	                showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	        },
	        function(){
	        	swal({
	                title: "Concesionario creado!",
	                text: "",
	                type: "success",
	                //showCancelButton: true,
	                //confirmButtonColor: "#DD6B55",
	                confirmButtonClass: "btn-danger",
	                confirmButtonText: "Aceptar",
	                //cancelButtonText: "Cancelar",
	                closeOnConfirm: false
	            },
	            function(){
	            	$('#formNewConcesionary').submit();
	            });

	        });

	}
});