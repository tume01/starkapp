// Submit post on submit
// $('#filters-form').on('submit', function(event){
//     submitFilters();
// });
//

$(document).ready(function() {
    refreshEvents();
});

function displayEvents(eventsData){

    $('#calendar').fullCalendar({
        defaultDate: '2016-05-01',
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        customButtons: {
            prev: {
                icon: 'left-single-arrow',
                click: function() {
                    prevMonth();
                    $('#calendar').fullCalendar( 'prev' )
//                        alert('clicked the custom button!');
                }
            },
            next: {
                icon: 'right-single-arrow',
                click: function() {
                    nextMonth();
                    $('#calendar').fullCalendar( 'next' )
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
        events: eventsData,
    });
}


$('#headquarter_id').change(function() {
    refreshEvents();
});

$('#bungalow_type_id').change(function() {
    refreshEvents();
});


function refreshEvents(){

    var requestData = {
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
//            console.log("AJAX REQUEST", data.events);
            displayEvents(data.events);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function prevMonth() {
    console.log('PREV Month')
    refreshEvents();
};

function nextMonth() {
    console.log('NEXT Month')
    refreshEvents();
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
}