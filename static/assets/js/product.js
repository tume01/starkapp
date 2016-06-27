$( document ).ready(function() {
	console.log( "product ready!" );

	$("#select2Provider").select2();
	$('#f_select2Provider').select2();
    //$(".js-example-basic-multiple").select2();

	console.log( "finish product ready!" );    
});

/*CODE FOR AJAX***************************************************/
function getCookie(c_name){
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

/******************************************************************/

$('#SaveProduct').click(function(){
	console.log('click Guardar');

	if ($('#name').val() == '' || $('#actualStock').val() == '' || $('#minStock').val() == '' ||
		$('#price').val() == '' || 
		$('#selectProductType').val() == '' || $('#selectProductType').val() == null){

		$('#formNewProduct').submit();
		//console.log('form');
		//console.log($('#selectProductType').val());
	}
	else if($('#actualStock').val() <= $('#minStock').val()){
		swal({
            title: "",
            text: "El stock actual debe superar al minimo.",
            type: "info"
        });
	}
	else{
		console.log('ajax');
		data = {};
		data.name = $('#name').val();
		data.actualStock = $('#actualStock').val();
		data.minStock = $('#minStock').val();
		data.productType = $('#selectProductType').val();
		data.description = $('#description').val();
		data.providers = $('#select2Provider').val();
		data.price = $('#price').val();

		console.log(data);

		var xhr = $.ajax({
		    type: "POST", 
		    url: "/products/create/insert/", //url que procesa
		    dataType: "text",
		    data: JSON.stringify(data),
		    contentType: "application/json; charset=utf-8",
	    });

		xhr.done(function(data) {
			console.log('done='+data);
			window.location = "/products";
	    });

	    xhr.fail(function(xhr, status, text){
	        console.log("Error " + xhr.readyState + " " +text);

	    });

	    return xhr;
	}
});


$('#EditProduct').click(function(){
	console.log('click editar');


	if ($('#name').val() == '' || $('#actualStock').val() == '' || $('#minStock').val() == '' ||
		$('#price').val() == '' || 
		$('#selectProductType').val() == '' || $('#selectProductType').val() == null){

		$('#formEditProduct').submit();
		//console.log('form');
		//console.log($('#selectProductType').val());
	}
	else if(parseInt($('#actualStock').val()) <= parseInt($('#minStock').val())){
		swal({
            title: "",
            text: "El stock actual debe superar al minimo.",
            type: "info"
        });
	}
	else{
		swal({
                title: "Edicion de producto",
                text: "Se actualizara el producto seleccionado. ¿Desea continuar?",
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
                title: "Producto actualizado!",
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
            	data = {};
				data.name = $('#name').val();
				data.actualStock = $('#actualStock').val();
				data.minStock = $('#minStock').val();
				data.productType = $('#selectProductType').val();
				data.description = $('#description').val();
				data.providers = $('#select2Provider').val();
				data.price = $('#price').val();

				console.log(data);

				var xhr = $.ajax({
				    type: "POST", 
				    url: "/products/edit/update/"+ $('#idProduct').val(), //url que procesa
				    dataType: "text",
				    data: JSON.stringify(data),
				    contentType: "application/json; charset=utf-8",
			    });

			    xhr.done(function(data) {
					console.log('done='+data);
					window.location="/products";
			    });

			    xhr.fail(function(xhr, status, text){
			        console.log("Error " + xhr.readyState + " " +text);

			    });
            	return xhr;
            });

            
		});
	}

});

$('#filterProduct').click(function(){
	console.log('click filtro');

	/*
	console.log('f_name='+$('#f_name').val());
	console.log('f_select2Provider='+$('#f_select2Provider').val());
	console.log('f_selectProductType='+$('#f_selectProductType').val());
	console.log('f_range_stock_min='+$('#f_range_stock_min').val());
	console.log('f_range_stock_max='+$('#f_range_stock_max').val());
	console.log('f_active='+$('#f_active').is(':checked'));
	console.log('f_range_price_min='+$('#f_range_price_min').val());
	console.log('f_range_price_max='+$('#f_range_price_max').val());
	*/

	data = {};

	data.f_name = $('#f_name').val();
	data.f_select2Provider = $('#f_select2Provider').val();
	data.f_selectProductType = $('#f_selectProductType').val();
	/*
	data.f_range_stock_min = $('#f_range_stock_min').val();
	data.f_range_stock_max = $('#f_range_stock_max').val();
	data.f_active = $('#f_active').val();
	data.f_range_price_min = $('#f_range_price_min').val();
	data.f_range_price_max = $('#f_range_price_max').val();
	*/

	console.log('json='+JSON.stringify(data));

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/products/filter/", //url que procesa
	    dataType: "text",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
    });

	xhr.done(function(data) {
		//console.log('done='+list); //data que recibes de controller
		var array_products = $.parseJSON(data);

		//$("#productsTable").empty(); //delete rows on table
		var contents = $("#productsTable").find('tbody').contents().detach();
		//addTableHeader();		
		
		for (var i=0; i<array_products.length; i++){
			var item = array_products[i];
			console.log(item);
			addRowsOnTable(item, i);
		}

		
		//window.location = "/products"; //url que abrira
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

    return xhr;

});

function addRowsOnTable(item, i){
	var textStatus = '';
	var color = '';

	if (item == 0) textStatus = 'Inactivo';
	else textStatus = 'Activo';

	if (i%2 != 0) color = '#FFF'; //color blanco para el td

	$("#productsTable")
    		.append($('<tbody>')
        		.append($('<tr>')
        			.css('background-color',color)
        			.append($('<td>')
                		.attr('class', 'text-center')
                		.text(item.id)
                	)
                	.append($('<td>')
                		.text(item.name)
                	)
                	.append($('<td>')
                		.text(item.price)
                	)
                	.append($('<td>')
                		.attr('class', 'hidden-xs')
                		.text(item.actual_stock)
                	)
                	.append($('<td>')
                		.text(item.minimum_stock)
                	)
                	.append($('<td>')
                		.text(textStatus)
                	)
                	.append($('<td>')
                		.attr('class', 'text-center')
                		.attr('style', 'width: 10%;')
                		.text(item.description)
                	)
                	.append($('<td>')
                		.attr('class', 'text-center')
                		.append($('<div>')
                			.attr('class', 'btn-group')
                			.append($('<a>')
                				.attr('href', '/products/edit/'+item.id)
                				.append($('<button>')
                					.attr('class', 'btn btn-xs btn-default')
                					.attr('type', 'button')
                					.attr('data-toggle', 'tooltip')
                					.attr('title', 'Editar Producto')
                					.append($('<i>')
                						.attr('class', 'fa fa-pencil')
                					)
                				)

                			)
                			.append($('<a>')
                				.attr('href', '/products/delete/update/'+item.id)
                				.append($('<button>')
                					.attr('class', 'btn btn-xs btn-default')
                					.attr('type', 'button')
                					.attr('data-toggle', 'tooltip')
                					.attr('title', 'Borrar Producto')
                					.append($('<i>')
                						.attr('class', 'fa fa-times')
                					)
                				)

                			)

                		)
                	)
        		)
    	);

}


function shopProduct(id, stock){
	console.log('shop product'+ id);

	swal({   
		title: "Ingrese la cantidad del producto",   
		//text: "Coloque un stock",   
		type: "input",   
		showCancelButton: true,   
		closeOnConfirm: false,   
		animation: "slide-from-top",   
		inputPlaceholder: "" 
	},
	function(inputValue){         
		if (!$.isNumeric(inputValue) || inputValue == "") {     
			swal.showInputError("Debe ingresar un numero");     
			return false;   
		}
		else{
			if (inputValue > stock){
				swal.showInputError("No hay stock suficiente");  
				return false;   
			}
			else{
				data = {};
				data.id = id;
				data.quantity = inputValue;
				console.log(data);

				var xhr = $.ajax({
				    type: "POST", 
				    url: "/products/make/purchase/", 
				    dataType: "json",
				    data: JSON.stringify(data),
				    contentType: "application/json; charset=utf-8",
			    });

				xhr.done(function(data) {
					console.log('done='+data); 
					swal({
		                title: "Compra exitosa!",
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
		            	window.location = "/products/index/shop/product";
		        	});
			    });

			    xhr.fail(function(xhr, status, text){
			        console.log("Error " + xhr.readyState + " " +text);

			    });

			    return xhr;	
			}
		}
		
	});
}

/*
$('#formNewProduct').submit(function(){
	console.log('form click');
	SaveProduct();
});
*/