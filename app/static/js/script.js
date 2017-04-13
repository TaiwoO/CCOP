//makes a map
//googlemaps automatically calls this
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

function initBarChart(labels, data)
{

}

//make a table

function initApp() {
    //initBarChart()
    initPieChart();
}

initApp()

console.log("SCRIPT WORKING!!")

