//Writen by Robert Bradshaw

//implements the map view

//googlemaps automatically calls this
function initMap()
{
    //console.log("initMap called");

    var minZoomLevel = 10;
    var latLng = { lat: 39.154743, lng: -77.240515 };
    window.map = new google.maps.Map(document.getElementById('map'),{
        zoom: minZoomLevel,
        center: latLng,
        scrollwheel: false,
        streetViewControl: false
    });

    google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
        // runs once the map loads
        updateMarkers();

        google.maps.event.addListener(map, 'bounds_changed', function() {
            // don't constantly update while user drags the map
            if(!window.isDragging){
                updateModules();
            }
        });
    });

    // track when the user is dragging
    google.maps.event.addListener(map, 'dragstart', function(){window.isDragging = true;});
    google.maps.event.addListener(map, 'dragend', function(){window.isDragging = false;});
        
}

// clears markers from the map
// stolen from stack overflow:
// http://stackoverflow.com/questions/1544739/google-maps-api-v3-how-to-remove-all-markers
function clearMarkers(){
    //console.log("clearMarkers called")
    var bounds = window.map.getBounds();
    for (var i = 0; i < window.mapMarkers.length; i++) {
        window.mapMarkers[i].setMap(null);
    }
    window.mapMarkers.length = 0;
}


//Gets markers onto map
function updateMarkers()
{
    //console.log("updateMarkers called");
    // clear out the old markers
    clearMarkers();

	var crime, latLng;
	for(i in window.crimeJSON){
	    //console.log(i);
	    crime = window.crimeJSON[i];
	    latLng = new google.maps.LatLng(crime.latitude, crime.longitude);

	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Crime\n"+crime.description+"\n"+crime.dispatch+"\n"+crime.street,
		label: "C"
	    });
            window.mapMarkers.push(marker);
        
	}
   
	var arrest;
	for(i in window.arrestJSON){
	    arrest = window.arrestJSON[i];
	    latLng = new google.maps.LatLng(arrest.latitude, arrest.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Arrest\n"+arrest.offense+"\n"+arrest.date+"\n"+arrest.street,
		label: "A"
	    });
            //marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png');
	    window.mapMarkers.push(marker);
	}


    
}

//limits the map
function limitMap(map, minZoomLevel)
{
    var opt = { minZoom: minZoomLevel};
    map.setOptions(opt);
    map.fitBounds();
}
//Filter markers
//get data from selected marker
