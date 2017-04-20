

// Return raw JSON from endpoint
function getJson(endpoint) {
    $.getJSON($SCRIPT_ROOT + endpoint,{}, function (data) {
        console.log(data);
    });
}

function initApp() {
    initCharts();
}

initApp()
//getJson("/crime")

console.log("SCRIPT WORKING!!")
console.log("IS IT, THO?")
