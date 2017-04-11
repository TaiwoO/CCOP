


// Open and close the side nav bar
$(document).ready(function () {
    $('#side-nav-btn').click(function () {
        var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
        $('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
});

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

//makes the charts
function initPieChart() {
    // Load the Visualization API and the corechart package.
    google.charts.load('current', { 'packages': ['corechart'] });

    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(drawChart);

    // Callback that creates and populates a data table,
    // instantiates the pie chart, passes in the data and
    // draws it.
    function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
            ['Mushrooms', 3],
            ['Onions', 1],
            ['Olives', 1],
            ['Zucchini', 1],
            ['Pepperoni', 2]
        ]);

        // Set chart options
        var options = {
            'title': 'How Much Pizza I Ate Last Night',
        };

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart'));
        chart.draw(data, options);
    }
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
