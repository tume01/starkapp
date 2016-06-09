$( document ).ready(function() {
	console.log( "bungalow service ready!" );

    $('#bungalow_type').select2({
        placeholder: 'Seleccione un tipo',
        minimumResultsForSearch: Infinity
    });

	$("#select2BungalowService").select2();

	console.log( "finish product ready!" );    
});


$('#bungalow_type').change(function(){
	console.log( "bungalow type change" );

	data = {};

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/bungalow_service/getServices/"+ $('#bungalow_type').val(), //url que procesa
	    dataType: "json",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
    });

    xhr.done(function(data) {
    	var list_services = data;

    	console.log('fill select2');

        if ($('#bungalow_type').val() > 0){
        	var array_id = [];
        	for (var i=0; i<list_services.length; i++) array_id.push(list_services[i].id);
        	
        	$('#select2BungalowService').val(array_id).change();
        }
        else{
            //var array_selected = $('#select2BungalowService').val();
            //console.log(array_selected);
        }
    

		//window.location="/products";
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

    return xhr;

});

$('#SaveServices').click(function(){
    console.log( "save service" );
});

$('#CancelSaveServices').click(function(){
    console.log( "cancel load service" );
    window.location = '/bungalows';
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

