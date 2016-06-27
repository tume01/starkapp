var actualPunctuation = -5;

$( document ).ready(function() {
	console.log( "punctuation ready!" );
	console.log( "finish punctuation ready!" ); 

	calculateActualPunctuation();

	executeAsync(function() {
    	/*Verify if punctuation is registered*/
    	
    	console.log('antes!');
    	console.log(actualPunctuation);
    	if(actualPunctuation == 0){
    		console.log('entro!');

	    	swal({   
	    		title: "Puntuacion!",   
	    		text: "Brindanos tu support: (1: Malo, 5:Muy Bueno)",   
	    		type: "input",   
	    		showCancelButton: true,   
	    		closeOnConfirm: false,   
	    		animation: "slide-from-top",   
	    		inputPlaceholder: "Write something" 
	    	}, function(inputValue){   
	    		if ($.isNumeric(inputValue)) {
	    			var points = parseInt(inputValue);
	    			if(points < 0 || points > 5){
	    				swal.showInputError("Debes colocar una puntuacion del 1 al 5!");     
	    				return false;
	    			}
	    			else{
	    				/*Register Punctuation*/
	    				registerPunctuation(points);
	    				swal("Muchas gracias!", "Tu puntuacion sera tomada en cuenta.", "success"); 
	    			}
	    		}
	    		else{
	    			swal.showInputError("Debes colocar una puntuacion del 1 al 5!");     
	    			return false;
	    		}     
	    		
	    	});
		}
		else console.log('no entro!');
	});
	

});

function executeAsync(func) {
	var time = 10000;
    setTimeout(func, time);
}

function calculateActualPunctuation(){
	var points = -1;
	var data = {};
	console.log(data);

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/members/calculate/punctuation/", //url que procesa
	    dataType: "json",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
	});

	xhr.done(function(data) {
		console.log(data);
		console.log("p="+data.document);
		actualPunctuation = parseInt(data.punctuation);
		//return points;
		//return parseInt(data.punctuation);
		//window.location = "/products";
	});

	xhr.fail(function(xhr, status, text){
	    console.log("Error " + xhr.readyState + " " +text);
	});

	return xhr;
	//return points;

}


function registerPunctuation(points){
	var data = {};
	data.points = points;

	var xhr = $.ajax({
	    type: "POST", 
	    url: "/members/register/punctuation/", //url que procesa
	    dataType: "json",
	    data: JSON.stringify(data),
	    contentType: "application/json; charset=utf-8",
	});

	xhr.done(function(data) {
		console.log(data);
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