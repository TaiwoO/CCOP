//Writen by Robert Bradshaw
//implements the map view

function getData(callback)
{
    $.getJSON("/crime");
}

//googlemaps automatically calls this
function initMap()
{
    var minZoomLevel = 10;
    var uluru = { lat: 39.154743, lng: -77.240515 };
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: minZoomLevel,
        center: uluru
    });
    
    getData(function(data){
	var crimes = data.crimes;
	var crime, latLng;
	for(i in crimes){
	    console.log(i);
	    crime = crimes[i];
	    latLng = new google.maps.LatLng(crime.latitude, crime.longitude);
	    
	    var marker = new google.maps.Marker({
		position:latLng,
		map: map
	    });
	}
    });
    
    limitMap(map,minZoomLevel);
    
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
