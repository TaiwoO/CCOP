s// Open and close the side nav bar
$(document).ready(function () {
    $('#side-nav-btn').click(function (){
	var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
	$('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
});

//timeline slider functionality
$(document).ready(function () {
    $(function() {
	$( "#slider-range" ).slider({
	    orientation: "horizontal",
	    range: true,
	    min: 0,
	    max: 100,
	    values: [ 0, 100 ],
	    slide: function( event, ui){
		if ((ui.values[0] + 1) >= ui.values[1]) {
		    return false;
		}
	    },
	    change: function( event, ui ){
		var vals = ui.values;
		console.log(vals);
	    }
	});
    } );
});
