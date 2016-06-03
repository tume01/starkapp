// Submit post on submit
$('#filters-form').on('submit', function(event){
    event.preventDefault();
    submit_filters();
});

$('#btn-edit').click(function(){
    console.log("BTN CLICK");
});


// {% url 'update_index' bungalow.id %}

function submit_filters() {
    console.log('Submit Filters')

    console.log($('#bungalow_type_id option:selected').val())
    console.log($('#member_name').val())
    console.log($('#headquarter_id option:selected').val())
    // var csrftoken = getCookie('csrftoken');
    // console.log(csrftoken)

    $.ajax({
        url : "post", // the endpoint
        type : "POST", // http method
        data : {
            'bungalow_type_id' : $('#bungalow_type_id option:selected').val(),
            'member_name' : $('#member_name').val(),
            'headquarter_id' : $('#headquarter_id option:selected').val(),
            'csrfmiddlewaretoken' :  getCookie('csrftoken')
            // '{% csrf_token %}'
        }, // data sent with the post request

        // handle a successful response
        success : function(data) {
            $('#table-content').html(data);
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
}