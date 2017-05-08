//Writen by Robert Bradshaw

//implements the map view

//googlemaps automatically calls this
function initMap()
{
    //console.log("initMap called");

    var minZoomLevel = 12;
    var latLng = { lat: 39.154743, lng: -77.240515 };
    window.map = new google.maps.Map(document.getElementById('map'),{
        zoom: minZoomLevel,
        center: latLng,
        scrollwheel: false,
        streetViewControl: false
    });

    /*
    google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
        // runs once the map loads
        updateMarkers();
    });
    */

    //idle event triggered after drag end and zoom in/out end
    google.maps.event.addListener(map, 'idle', function() {
        // don't constantly update while user drags the map
        if(!window.isDragging){
            updateModules();
        }
    });

    // track when the user is dragging
    google.maps.event.addListener(map, 'dragstart', function(){window.isDragging = true;});
    google.maps.event.addListener(map, 'dragend', function(){window.isDragging = false;});


    var legend = window.legend;
    var div = document.createElement('div');
    div.innerHTML = "<h3>Legend</h3>";
    legend.appendChild(div);
    var icons =
	{
            crime: {
		name: 'Crime',
		icon: "/static/images/blue_MarkerC.png"
            },
            arrest: {
		name: 'Arrest',
		icon:  "/static/images/red_MarkerA.png"
            }
	};
    
    //add a key to the side
    
        for (var key in icons) {
          var type = icons[key];
          var name = type.name;
          var icon = type.icon;
          div = document.createElement('div');
          div.innerHTML = '<br><img src= "' + icon + '"> ' + name;
          legend.appendChild(div);
        }

        map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
        
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
    var crime, latLng, arrest,length,crimeLength,arrestLength;
    var crimeIcon = "/static/images/blue_MarkerC.png";
    var arrestIcon = "/static/images/red_MarkerA.png";
    crimeLength = window.crimeJSON.length;
    arrestLength = window.arrestJSON.length;
    
    if(arrestLength > crimeLength)
    {
	length = arrestLength;
    }
    else
    {
	length = crimeLength;
    }

    //loop over the length of the larger dataset
    for(i = 0; i < length; i++)
    {
	//console.log(i);
	if(i < crimeLength)
	{
	    crime = window.crimeJSON[i];
	    latLng = new google.maps.LatLng(crime.latitude, crime.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Crime\n"+crime.description+"\n"+crime.dispatch+"\n"+crime.street,
		icon: crimeIcon
	    });
	    //clicking the marker will call the highlight row function from Table.js
	    marker.addListener('click', function() {
		highlightRow(crime.id);
            });
	    
            window.mapMarkers.push(marker);
	}
	if(i < arrestLength)
	{
            arrest = window.arrestJSON[i];
	    latLng = new google.maps.LatLng(arrest.latitude, arrest.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Arrest\n"+arrest.offense+"\n"+arrest.date+"\n"+arrest.street,
		icon:arrestIcon
	    });
	    //clicking the marker will call the highlight row function from Table.js
	    marker.addListener('click', function() {
		highlightRow(arrest.id);
            });
	    window.mapMarkers.push(marker);
	}
    }
}
