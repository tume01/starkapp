$( document ).ready(function() {
	console.log( "bungalow reservation user ready!" );

    $('#bungalow').select2({
        placeholder: 'Seleccione un bungalow',
        minimumResultsForSearch: Infinity
    });

	$("#select2BungalowService").select2();

	console.log( "finish product ready!" );    
});

$('#bungalow').change(function(){
	console.log( "services aditional on bungalow" );

    data = {};

    console.log(data);

    var xhr = $.ajax({
        type: "POST", 
        url: "/bungalowReservations/filter/aditional/services/"+ $('#bungalow').val(), //url que procesa
        dataType: "json",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
    });

    xhr.done(function(data) {
        //window.location="/bungalow_service";
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

    return xhr;

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