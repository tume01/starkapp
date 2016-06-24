$( document ).ready(function() {
	console.log( "bungalow reservation user ready!" );

    $('#bungalow').select2({
        placeholder: 'Seleccione un bungalow',
        minimumResultsForSearch: Infinity
    });


	$("#select2BungalowService").select2();
    $("#select2BungalowServiceAdd").select2({
        placeholder: 'Seleccione un servicio',
        minimumResultsForSearch: Infinity
    });

	console.log( "finish product ready!" );    
});

$('#bungalow').change(function(){
	console.log( "services aditional on bungalow" );

    var data = {};

    console.log(data);

    var xhr = $.ajax({
        type: "POST", 
        url: "/bungalowReservations/filter/aditional/services/"+ $('#bungalow').val(), //url que procesa
        dataType: "json",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
    });

    xhr.done(function(data) {
        console.log(data);
        if ($('#bungalow').val() > 0){
            var array_id_actual = [];
            for (var i=0; i<data.actual_serv.length; i++) 
                array_id_actual.push(data.actual_serv[i].id);
            
            $('#select2BungalowService').val(array_id_actual).change();

            $("#select2BungalowServiceAdd").html('').select2({data: data.all_serv}); 

            var array_id_reservation_serv = [];
            for(var i=0; i<data.reservation_serv.length; i++) 
                array_id_reservation_serv.push(data.reservation_serv[i].id);

            if(data.reservation_serv.length > 0){
                $('#select2BungalowServiceAdd').val(array_id_reservation_serv).change();
                $('#select2BungalowServiceAdd').attr('disabled', 'disabled');
                console.log("disable");
            }
            else{
                $('#select2BungalowServiceAdd').removeAttr('disabled');
                console.log("enable");
            }
        }
        
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

    return xhr;

});

$('#SaveExtraServices').click(function(){
    console.log("save extra service");
    var data = {};
    data.services = $('#select2BungalowServiceAdd').val()
    console.log(data);

    //$('#modalSaveAddService>p').html('Use this text as modal heading');
    //$('#modalSaveAddService').show();
    

    var xhr = $.ajax({
        type: "POST", 
        url: "/bungalowReservations/save/aditional/services/"+ $('#bungalow').val(), //url que procesa
        dataType: "json",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
    });

    xhr.done(function(data) {
        console.log(data);
        console.log("saved!");
        
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