// Open and close the side nav bar
$(document).ready(function () {
    $('#side-nav-btn').click(function (){
	var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
	$('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
});


var minDate = Date.parse("2017-03-15 14:08:00");
var maxDate = Date.parse("2017-04-16 20:00:00");

//timeline slider functionality
$(document).ready(function () {
    $(function() {
	$( "#slider-range" ).slider({
	    orientation: "horizontal",
	    range: true,
	    min: minDate,
	    max: maxDate,
	    values: [ minDate, maxDate ],
	    slide: function( event, ui){
		//prevents complete overlap of slider handles
		if ((ui.values[0] + 10) >= ui.values[1]) {
		    return false;
		}
	    },
	    change: function( event, ui ){
		var vals = ui.values;
		console.log(vals);
		console.log(Date(ui.values[0]));
		console.log(Date(ui.values[1]));
	    }
	});
    } );
});
