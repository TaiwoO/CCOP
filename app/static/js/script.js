// Return raw JSON from endpoint
function getJson(endpoint) {
    $.getJSON($SCRIPT_ROOT + endpoint,{}, function (data) {
        console.log(data);
    });
}

function initApp() {
    initCharts();
}

initApp();
getJson("/crime?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342");

console.log("SCRIPT WORKING!!");
console.log("IS IT, THO?");
