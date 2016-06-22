

$('#headquarter_id').on('change', function(event){
    var req_data = submitFilters();
    chargeEnvironments(req_data);
});

$('#environment_id').on('change', function(event){
    $('#calendar').fullCalendar( 'refetchEvents' );
});


$(document).ready(function() {
    $('#calendar').fullCalendar({
        defaultDate: new Date(),
        editable: true,
        allDayDefault: true,
        defaultView: "month",
        eventLimit: true, // allow "more" link when too many events
        events: function(start, end, timezone, callback){
            var startDate = new Date(start);
            var endDate = new Date(end);
            endDate.setDate(endDate.getDate() - 1);
            var currentDate = new Date()
            if (startDate < currentDate) startDate = currentDate
//            Debido al TimeZone
            startDate.setHours(startDate.getHours() - 5);

            refreshEvents(startDate, endDate, callback);
        },
        eventClick: function(calEvent, jsEvent, view) {
//            TODO: Reserve a Bungalow with current filters
            var href2 = '{% url "environments:index_book" %}'
            console.log(href2)
            console.log(calEvent)
//            location.href = '{% url "bungalowReservation:index" %}';
        }
    });
});

function createReservation(){

}



function submitFilters() {
    // event.preventDefault();

    var requestData = getFilters();
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');
    return requestData;
};

//General filter
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




function refreshEvents(start, end, callback){
    console.log("Refresh Events");
    var requestData = {
        'start' : Math.floor(start.getTime()/1000),
        'end' : Math.floor(end.getTime()/1000),
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'environment_id' : $('#environment_id option:selected').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {
            console.log("AJAX REQUEST", data.events);
            callback(data.events);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}


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