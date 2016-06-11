// Submit post on submit
$('#filters-form').on('submit', function(event){
    submitFilters();
});

// Prevent Default Current Page
$( "#current-page" ).click(function(event) {
    event.preventDefault();
    console.log('CURRENT')
});

function submitFilters() {
    // event.preventDefault();

    var requestData = getFilters();
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');

    reloadTable(requestData);
};

function prevPage() {
    console.log('PREV Page')
    event.preventDefault();

    var requestData = getFilters();
    requestData.page = $('#page').text() - 1;
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');
    
    reloadTable(requestData);
};

function nextPage() {
    console.log('NEXT Page')
    event.preventDefault();
    
    var requestData = getFilters();
    requestData.page = parseInt($('#page').text(),10) + 1;
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');
    
    reloadTable(requestData);
};

function getFilters() {
    var filter = {
        'env_name'       : $('#env_name').val(),
        'environment_id' : $('#environment_id option:selected').val(),
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'start_date'     : $('#start_date').val(),
        'end_date'       : $('#end_date').val(),
    }
    return filter;
};

function reloadTable(requestData){
    $.ajax({
        url : "book/create/post", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#table-content').html(response);

            // Prevent Default Current Page
            $( "#current-page" ).click(function(event) {
                console.log('CURRENT')
            });
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
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