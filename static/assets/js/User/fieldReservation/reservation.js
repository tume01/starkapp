$(document).ready(function(){
    $('#headquarter_id').change(function() {
        refreshField();
    });
    //
    $('input[id=arrival_date]').change(function() {
        refreshField();
    });

    $('#start_hour').change(function(){
        refreshHours();
    });

    $('#reserved_hours').change(function(){
        refreshTime();
    });

});

function refreshField(){

    var requestData = {
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'arrival_date' : $('#arrival_date').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    console.log(requestData);

    $.ajax({
        url : "create/refresh_field", 
        type : "POST", 
        data : requestData, 


        success : function(data) {

            $('#environment_id').html(data);
            $('#stay_content').prop('disabled', true);
            $('#start_hour').prop('disabled', true);
            $('#environment_content').prop('disabled', true);
        },

        error : function(xhr,errmsg,err) {
            console.log("ERROR"); 
        }
    });
}

function refreshHours(){

    var requestData = {
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh_hour", 
        type : "POST", 
        data : requestData, 


        success : function(data) {

            $('#start_hour').prop('disabled', true);
        },


        error : function(xhr,errmsg,err) {
            console.log("ERROR"); 
        }
    });
}

function refreshTime(){

    var requestData = {
        'start_hour' : $('#start_hour').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    $.ajax({
        url : "create/refresh_max_time", 
        type : "POST", 
        data : requestData, 


        success : function(data) {


            $('#start_hour').html(data);
        },


        error : function(xhr,errmsg,err) {
            console.log("ERROR"); 
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