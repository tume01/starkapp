$(document).ready(function() {
    $('#calendar').fullCalendar({
        defaultDate: new Date(),
        editable: true,
        defaultView: "month",
        eventLimit: true, // allow "more" link when too many events
        events: function(start, end, timezone, callback){
            var date = new Date(start);
            console.log(start.toDate().toUTCString());
            console.log("Current: ", date, date.getMonth(), date.getFullYear());
            date.setDate(date.getDate() + 1);
            console.log("New: ", date, date.getMonth(), date.getFullYear());
            var month = date.getMonth();
            var year = date.getFullYear();
            refreshEvents(start, end, callback);
        }
    });
});

$('#headquarter_id').change(function() {
    $('#calendar').fullCalendar( 'refetchEvents' );
});

$('#bungalow_type_id').change(function() {
    $('#calendar').fullCalendar( 'refetchEvents' );
});

function refreshEvents(start, end, callback){
    console.log("Refresh Events");
    var requestData = {
        'start' : start/1000,
        'end' : end/1000,
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'bungalow_type_id' : $('#bungalow_type_id option:selected').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh_events", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {
            console.log("AJAX REQUEST", data.events);
            callback(data.events);

        },
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
}