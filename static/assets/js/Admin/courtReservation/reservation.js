// Submit post on submit
// $('#filters-form').on('submit', function(event){
//     submitFilters();
// });
//

$(document).ready(function() {

    $('#calendar').fullCalendar({
        defaultDate: new Date(),
        editable: true,
        defaultView : 'agendaWeek',
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


function displayEvents(data){
    console.log('displayEvents',data.month);

    $("#calendar").fullCalendar('removeEvents');
    $("#calendar").fullCalendar('addEventSource', data.events);
    $('#calendar').fullCalendar( 'gotoDate', data.month )
}


$('#headquarter_id').change(function() {
    var date = getCalendarDate();
    refreshEvents(date.getDate() ,date.getMonth(), date.getFullYear());
});


function refreshEvents(day,month,year){

    console.log(day,month,year)
    var requestData = {
        'dat'   : day,
        'month' : month + 1,
        'year' : year,
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh_events", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request
        // handle a successful response
        success : function(data) {
//            console.log("AJAX REQUEST", data.events);
            displayEvents(data);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function today() {

    var date = new Date();
    refreshEvents(date.getDate(),date.getMonth(), date.getFullYear());
};

function prevMonth() {
    var date = getCalendarDate();
    date.setMonth(date.getDate() - 7);
    refreshEvents(date.getDate(),date.getMonth(), date.getFullYear());
};
  
function nextMonth() {
    var date = getCalendarDate();
    date.setMonth(date.getDate() + 7);
    refreshEvents(date.getDate(),date.getMonth(), date.getFullYear());
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
