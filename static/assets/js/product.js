$( document ).ready(function() {
    console.log( "product ready!" );

   $("#select2Provider").select2();
    //$(".js-example-basic-multiple").select2();
});

/*CODE FOR AJAX*/
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

/**/

$('#SaveProduct').click(function(){
	console.log('click Guardar');
	data = {};
	data.name = $('#name').val();
	data.actualStock = $('#actualStock').val();
	data.minStock = $('#minStock').val();
	data.productType = $('#selectProductType').val();
	data.description = $('#description').val();
	data.providers = $('#select2Provider').val();
	data.price = $('#price').val();

	//data.csrfmiddlewaretoken = '{% csrf_token %}';


	console.log(data);

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/products/create/insert/", //url que procesa
	    dataType: "text",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
    });

	xhr.done(function(data) {
		//window.location="/professor/courses/topic/"+$("#topicId").val()+"/"+$("#courseId").val();
		//window.location="/professor/courses/6/edit";
		console.log('done='+data);
		//window.location="/professor/courses/topic/"+$("#topicId").val()+"/"+$("#courseId").val();
		//window.location="/professor/courses/"+$("#topicId").val()+"/edit";
    });

    xhr.fail(function(xhr, status, text){
        console.log("Error " + xhr.readyState + " " +text);

    });

    return xhr;
});