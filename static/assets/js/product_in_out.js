$( document ).ready(function() {
	console.log( "product in out ready!" );

	$('#selectMove').select2({
        placeholder: 'Seleccione un Movimiento',
        minimumResultsForSearch: Infinity
    });

    $('#selectProduct').select2({
        placeholder: 'Seleccione un Producto',
        minimumResultsForSearch: Infinity
    });

	console.log( "finish product ready!" );    
});

$('#RegisterMove').click(function(){
	var data = {};
	data.quantity = $('#quantity').val();
	data.move = $('#selectMove').val();
	console.log(data);
	console.log($('#selectProduct').val());

	var xhr = $.ajax({
        type: "POST", 
        url: "/products/register_in_out/"+ $('#selectProduct').val(), //url que procesa
        dataType: "json",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
    });

    xhr.done(function(data) {
    	console.log("send="+data);
    	console.log(data.status);

    	if (parseInt(data) > 0){ //error
    		alert('Cantidad excede el stock actual. Stock actual: ' + data);
    	}



        //window.location="/bungalow_service";
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

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
