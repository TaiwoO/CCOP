//Writen by Robert Bradshaw

//implements the map view

//googlemaps automatically calls this
function initMap()
{
    var minZoomLevel = 10;
    var uluru = { lat: 39.154743, lng: -77.240515 };
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: minZoomLevel,
        center: uluru
    });

    updateMarkers(map);
              
    //limitMap(map,minZoomLevel);
    
}

//Gets markers onto map
function updateMarkers(map)
{
    var url = "/crime?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342";
    $.getJSON($SCRIPT_ROOT+url,{}, function (data){
        console.log(data);
	var crimes = data.crimes;
	var crime, latLng;
	for(i in crimes){
	    //console.log(i);
	    crime = crimes[i];
	    latLng = new google.maps.LatLng(crime.latitude, crime.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Crime\n"+crime.description+"\n"+crime.dispatch+"\n"+crime.street,
		label: "C"
	    });
	}
    });

    url = "/arrest?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342";
    $.getJSON($SCRIPT_ROOT+url,{}, function (data){
        console.log(data);
	var arrests = data.arrests;
	var arrest, latLng;
	for(i in arrests){
	    console.log(i);
	    arrest = arrests[i];
	    latLng = new google.maps.LatLng(arrest.latitude, arrest.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map,
		title: "Arrest\n"+arrest.date+"\n"+arrest.street,
		label: "A"
	    });
	}
    });
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
