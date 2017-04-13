//Writen by Robert Bradshaw
//implements the map view


//googlemaps automatically calls this
function initMap()
{
    var minZoomLevel = 10;
    var uluru = { lat: 39.154743, lng: -77.240515 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: minZoomLevel,
        center: uluru
    });
 
    
    new google.maps.Marker({
        position: uluru,
        map: map
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
