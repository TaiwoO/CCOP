//Writen by Robert Bradshaw

//implements the map view

// Google map automatically calls this function
function initMap()
{
    var uluru = { lat: 39.154743, lng: -77.240515 };
    var map = new google.maps.Map(document.getElementById('map'), {
	zoom: 12,
	center: uluru
    });
    var marker = new google.maps.Marker({
	position: uluru,
	map: map
    });
}   
