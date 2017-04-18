
function initBarChart(labels, data)
{

}

//make a table

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

