// Submit post on submit
// $('#filters-form').on('submit', function(event){
//     submitFilters();
// });
//

$(document).ready(function() {
    today();
});

function displayEvents(data){
    console.log('displayEvents');

    $('#calendar').fullCalendar({
        defaultDate: data.month,
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
        },
//        dayClick: function(date, jsEvent, view) {
//
//            alert('Clicked on: ' + date.format());
//
//            alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
//
//            alert('Current view: ' + view.name);
//
//            // change the day's background color just for fun
//            $(this).css('background-color', 'red');
//        },
        events: data.events,
    });
}


$('#headquarter_id').change(function() {
    var date = getCalendarDate();
    refreshEvents(date.getMonth(), date.getFullYear());
});

$('#bungalow_type_id').change(function() {
    var date = getCalendarDate();
    refreshEvents(date.getMonth(), date.getFullYear());
});


function refreshEvents(month,year){

    console.log(month,year)
    var requestData = {
        'month' : month,
        'year' : year,
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
    console.log(date);

    return date;
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