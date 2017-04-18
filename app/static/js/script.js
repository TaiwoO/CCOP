
function initBarChart(labels, data)
{

}

//make a table

// Open and close the side nav bar
$(document).ready(function () {
    $('#side-nav-btn').click(function () {
        var sideNavWidth = $("#nav-side-menu").width() == 0 ? "400px" : "0px";
        $('#nav-side-menu').animate({ width: sideNavWidth }, 10);
    });
});

// Return raw JSON from endpoint
function getJson(endpoint) {
    $.getJSON($SCRIPT_ROOT + endpoint,{}, function (data) {
        console.log(data);
    });
}

function initApp() {
    initPieChart();
}

initApp()
getJson("/crime")

console.log("SCRIPT WORKING!!")
console.log("IS IT, THO?")

