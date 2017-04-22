/*
  filtermenu.js contains functions pertaining to the interactive elements on the filter menu toggled by the filter button in the top-right of the interface.
  
  includes:
  crimes
  cities
  timeline
  ---with updated date divs for time range display


*/


// Open and close the side nav bar
function setupSidebarAnimation(){
    $('#side-nav-btn').click(function (){
	var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
	$('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
}

//functions zeroPad and formatDT for date formatting from
//http://stackoverflow.com/questions/10466851/javascript-slider-that-scrolls-along-both-dates-and-times
function zeroPad(num, places) {
    var zero = places - num.toString().length + 1;
    return Array(+(zero > 0 && zero)).join("0") + num;
}

function formatDT(__dt) {
    var year = __dt.getFullYear();
    var month = zeroPad(__dt.getMonth()+1, 2);
    var date = zeroPad(__dt.getDate(), 2);
    var hours = zeroPad(__dt.getHours(), 2);
    var minutes = zeroPad(__dt.getMinutes(), 2);
    var seconds = zeroPad(__dt.getSeconds(), 2);
    return year + '-' + month + '-' + date + ' ' + hours + ':' + minutes + ':' + seconds;
}


var minDateString = "";
var maxDateString = "";

var minDateVal = 0;
var maxDateVal = 0;

//update date range values using values from sqlite db
function updateDateBounds(){
	//console.log("executing updateDateBounds");
	minDateVal = window.minDate/1000;
	maxDateVal = window.maxDate/1000;

	//initTimeline call is in here for synchronization purposes.
	initTimeline();
}

//initialize timeline slider and date range div(s) properties
function initTimeline(){

    minDateString = formatDT(window.minDate);
    maxDateString = formatDT(window.maxDate);
    
    $('.slider-time1').html(minDateString);
    $('.slider-time2').html(maxDateString);
    
    //timeline slider functionality
    //should call update functions when changes are detected
    $(document).ready(function () {
	$(function() {
	    $( "#slider-range" ).slider({
		orientation: "horizontal",
		range: true,
		min: minDateVal,
		max: maxDateVal,
		step: 1,
		values: [ minDateVal, maxDateVal ],
		slide: function( event, ui){
		    minDateString = formatDT(new Date(ui.values[0] * 1000));
		    maxDateString = formatDT(new Date(ui.values[1] * 1000));
		    $('.slider-time1').html(minDateString);
		    $('.slider-time2').html(maxDateString);
		},
		change: function( event, ui ){
		    window.minDate = new Date(ui.values[0] * 1000);
		    window.maxDate = new Date(ui.values[1] * 1000);
		    //console.log(window.minDate);
		    //console.log(window.maxDate);
		    updateModules();
		}
	    });
	} );
    });
}
