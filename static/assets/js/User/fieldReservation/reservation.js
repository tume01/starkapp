$('#headquarter_id').change(function() {
    refreshField();
});
//
$('input[id=arrival_date]').change(function() {
    refreshField();
});

$('#environment_content').change(function(){
    refreshHours();
});

$('#stay_content').change(function(){
    refreshTime();
});

function refreshField(){

    var requestData = {
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'arrival_date' : $('#arrival_date').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    //console.log("AJAX REQUEST", requestData)
    $.ajax({
        url : "create/refresh_field", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {

    //console.log("AJAX REQUEST", requestData)
            $('#environment_id').html(data);
            $('#reserved_hours').prop('disabled', true);
            $('#start_hour').prop('disabled', true);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function refreshHour(){

    var requestData = {
        'environment_content' : $('#environment_content').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    //console.log("AJAX REQUEST", requestData)
    $.ajax({
        url : "create/refresh_hour", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {

    //console.log("AJAX REQUEST", requestData)
            $('#environment_id').html(data);
            $('#reserved_hours').prop('disabled', true);
            $('#start_hour').prop('disabled', true);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function refreshTime(){

    var requestData = {
        'stay_content' : $('#stay_content').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    //console.log("AJAX REQUEST", requestData)
    $.ajax({
        url : "create/refresh_max_time", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {

    //console.log("AJAX REQUEST", requestData)
            $('#stay_content').html(data);
            $('#reserved_hours').prop('disabled', true);
            $('#start_hour').prop('disabled', true);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}