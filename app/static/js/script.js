


// Open and close the side nav bar
$(document).ready(function () {
    $('#side-nav-btn').click(function () {
        var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
        $('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
});

//makes a map
import {initMap} from 'Map.js';

//makes the charts
import {initPieChart} from 'Chart.js';

//makes the table




function initBarChart(labels, data) {

}

function initApp() {
    //initBarChart()
    initPieChart();
}

initApp()

console.log("SCRIPT WORKING!!")
