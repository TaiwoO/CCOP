// Return raw JSON from endpoint
function getJson(endpoint) {
    $.getJSON($SCRIPT_ROOT + endpoint,{}, function (data) {
        console.log(data);
    });
}

// when the page loads
$(document).ready(function () {
    //console.log("window ready");
    // enable the menu animations
    setupSidebarAnimation();

    // setup chart view
    initCharts();

    // setup table view
    initTables();

    // look up the min and max dates for the range slider
    $.getJSON("http://localhost:5000/range", function(data){
	    window.minDate = new Date(data["min"]);
	    window.maxDate = new Date(data["max"]);
        
        // update the time slider boundary values
        updateDateBounds();

        // initialize the map, chart, and tabular views
        updateModules();
    });
    
    
});


function updateModules(){
    // first read the values to filter on
    // time
    var minTime = "min_time=" + window.minDate.toJSON();
    var maxTime = "&max_time=" + window.maxDate.toJSON();
    // TODO implement city filtering

    // TODO implement crime type filtering

    // read the map bounding box
    // the map is loaded asynchronous and deferred, so it usually isn't loaded by now
    // which means that we need a default window for when that happens
    var mapLoaded = map.getBounds();
    if(mapLoaded === undefined) {
        var bounds = "&bounds=38.836685,-77.892142,39.47137,-76.588888";
    } else {
        // map has already been loaded
        var bounds = "&bounds=" + mapLoaded.toUrlValue();
    }

    var query = "?" + minTime + maxTime + bounds;

    //console.log(query);

    // then, make requests to the endpoints to get the new data

    $.getJSON($SCRIPT_ROOT + "/crime" + query, function (crimeData){
        
        $.getJSON($SCRIPT_ROOT + "/arrest" + query, function (arrestData){
            
            window.crimeJSON = crimeData.crimes;
            window.arrestJSON = arrestData.arrests;

            // reload the markers if the map has already been loaded
            if(mapLoaded !== undefined){
                updateMarkers();
            }

            // update the charts
            drawPieChart(query);
            

        });

    });

    // finally, outsource the updating of each module
}

//initApp();
//getJson("/crime?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342");

//console.log("SCRIPT WORKING!!");
//console.log("IS IT, THO?");
