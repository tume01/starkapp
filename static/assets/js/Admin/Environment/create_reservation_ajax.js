// Submit post on submit
$('#filters-form').on('submit', function(event){
    var req_data = submitFilters();
    verifyDay(req_data);
});

$('#insert-form').on('submit', function(event){
    var req_data = submitFilters();
    insertReservation(req_data);
});


$('#headquarter_id').on('change', function(event){
    var req_data = submitFilters();
    chargeEnvironments(req_data);
});



function submitFilters() {
    // event.preventDefault();

    var requestData = getFilters();
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');
    return requestData;
};

function chargeEnvironments(requestData) {    
    $.ajax({
        url : "create/getEnvs", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#select_env').html(response);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function getFilters() {
    var filter = {
        'env_name'       : $('#env_name').val(),
        'environment_id' : $('#environment_id option:selected').val(),
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'start_date'     : $('#start_date').val(),
        'end_date'       : $('#end_date').val(),
        'price'          : $('#price').val(),
    }
    return filter;
};

function verifyDay(requestData){
    $.ajax({
        url : "create/post", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#form-content').html(response);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function insertReservation(requestData){
    $.ajax({
        url : "create/insert", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(response) {
            console.log("SUCCESS");
            window.location.href = response;
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};