function averageP(){
	console.log('average');

	var data = {};

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/members/average/punctuation/", //url que procesa
	    dataType: "json",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
	});

	xhr.done(function(data) {
		console.log(data);
		swal("Puntuación promedio!", "Hasta este momento: "+data.average+ " ptos.", "success")
	});

	xhr.fail(function(xhr, status, text){
	    console.log("Error " + xhr.readyState + " " +text);
	});

	return xhr;
}


/*CODE FOR AJAX***************************************************/
function getCookie(c_name){
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

/******************************************************************/