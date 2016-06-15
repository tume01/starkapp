

$('#headquarter_id').on('change', function(event){
    var req_data = submitFilters();
    chargeEnvironments(req_data);
});

$('#environment_id').on('change', function(event){
    var date = getCalendarDate();
    refreshEvents(date.getMonth(), date.getFullYear());
});


$(document).ready(function() {

    $('#calendar').fullCalendar({
        defaultDate: new Date(),
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        customButtons: {
            prev: {
                icon: 'left-single-arrow',
                click: function() {
                    prevMonth();
                }
            },
            next: {
                icon: 'right-single-arrow',
                click: function() {
                    nextMonth();
                }
            }
        }
    });

    today();
});





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




function refreshEvents(month,year){

    console.log(month,year)
    var requestData = {
        'month' : month + 1,
        'year' : year,
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'environment_id' : $('#environment_id option:selected').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh_events", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {
            console.log("AJAX REQUEST", data.events);
            displayEvents(data);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function today() {
//    $('#calendar').fullCalendar( 'prev' );
    var date = new Date();
    console.log(date);
    refreshEvents(date.getMonth(), date.getFullYear());
};

function prevMonth() {
//    $('#calendar').fullCalendar( 'prev' );
    var date = getCalendarDate();
    date.setMonth(date.getMonth() - 1);
    refreshEvents(date.getMonth(), date.getFullYear());
};

function nextMonth() {
//    $('#calendar').fullCalendar( 'next' );
    var date = getCalendarDate();
    date.setMonth(date.getMonth() + 1);
    refreshEvents(date.getMonth(), date.getFullYear());
};


function getCalendarDate(){
    var date = $('#calendar').fullCalendar('getDate').toDate();
    date.setDate(date.getDate() + 1);

    return date;
}

function displayEvents(data){
    console.log('displayEvents',data.month);

    $("#calendar").fullCalendar('removeEvents');
    $("#calendar").fullCalendar('addEventSource', data.events);
    $('#calendar').fullCalendar( 'gotoDate', data.month );
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