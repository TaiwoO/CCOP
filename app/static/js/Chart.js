"use strict"
//written by Taiwo
//will implement the Chart
// This file construct the charts of the application

var piechartData, piechart;
var linechartData, linechart;


// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['corechart'] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(initPieChart);


// Set a callback to run when the Google Visualization API is loaded.
// google.charts.setOnLoadCallback(drawHistrogram);

google.charts.setOnLoadCallback(initLineChart);


// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function initPieChart() {

    $.getJSON($SCRIPT_ROOT + "/crime/type", {}, function (result) {
        piechartData = new google.visualization.DataTable();
        piechartData.addColumn('string', 'Crime Type')
        piechartData.addColumn('number', 'frequency');

        var crimeTypes = result.crime_types;
        for (var type in crimeTypes) {
            piechartData.addRow([type, crimeTypes[type]]);
        }

        // Set chart options
        var options = {
            title: 'Crime types',
            pieHole: 0.4,
            width: 600,
            height: 600,
            enableInteractivity: false,
            fontSize: 16,
            legend: {textStyle: {fontSize: 16}}
        };
        // Instantiate and draw our chart, passing in some options.
        piechart = new google.visualization.PieChart(document.getElementById('piechart'));
        google.visualization.events.addListener(piechart, 'select', selectHandler);
        piechart.draw(piechartData, options);
    });
}

function updatePieChart(query) {

    if (query === undefined)
        query = "";

    $.getJSON($SCRIPT_ROOT + "/crime/type" + query, {}, function (result) {

        var crimeTypes = result.crime_types;

        //Check if empty
        var empty = true;
        for (var key in crimeTypes) {
            if (crimeTypes[key] > 0) {
                empty = false;
            }
        }

        // if (empty) {
        //     $("#piechart").hide();
        //     $("#no-data-piechart").show();
        //     return;
        // } 
        // else {
        //     $("#piechart").show();
        //     $("#no-data-piechart").hide();
        // }

        // Chart must exisit before it is updated
        if (piechart) {

            // Clear the data set
            while (piechartData.getNumberOfRows() > 0) {
                piechartData.removeRow(0)
            }

            // Add new data to dataset
            for (var type in crimeTypes) {
                piechartData.addRow([type, crimeTypes[type]]);
            }

            var title = "Crime Types"
            if (empty)
                title = "No Crime Data to Display"
            var options = {
                title: title,
                pieHole: 0.4,
                width: 600,
                height: 600,
                enableInteractivity: false,
                fontSize: 16,
                legend: {textStyle: {fontSize: 16}}

            };

            piechart.draw(piechartData, options);

        }
    });
}

// Handles what happens after a user clicks on the piechart
function selectHandler() {
    var selectedItem = piechart.getSelection()[0];
    if (selectedItem) {
        var value = piechartData.getValue(selectedItem.row, 0);
        console.log('The user selected ' + value);
    }
    else {
        console.log("deselected???")
    }

}

function initLineChart() {
    linechartData = new google.visualization.DataTable();
    linechartData.addColumn('date', 'Arrest')
    linechartData.addColumn('number', 'Arrests');
    // linechartData.addColumn('number', 'The Avengers');

    linechart = new google.visualization.LineChart(document.getElementById('histogram'));

    // linechart = new google.visualization.Histogram(document.getElementById('histogram'));

    if (window.arrestJSON && window.crimeJSON)
        updateLineChart(window.crimeJSON, window.arrestJSON)

}

function updateLineChart(crimes, arrests) {
    var dateofCrime = {};
    var dateOfArrest = {};
    var totalArrests = arrests.length;
    var totalCrimes = crimes.length;

    // if (totalArrests == 0 || totalCrimes == 0) {
    //     $(function () {
    //         $("#histogram").text("NO DATA");
    //     })
    //     return;
    // }

    // Get the frequency of arrests for each distinct date. 
    for (let i in arrests) {

        // date must exisit
        if (arrests[i].date) {
            var mdyOfArrest = new Date(arrests[i].date).toJSON().slice(0, 10) // get only month, date, and year
            if (mdyOfArrest in dateOfArrest)
                dateOfArrest[mdyOfArrest] += 1;
            else {
                dateOfArrest[mdyOfArrest] = 1;
            }
        }
    }

    // Get the frequency of crime for crime date matching arrest date. 
    for (let i in crimes) {
        if (crimes[i].dispatch) {

            var mdyOfCrime = new Date(crimes[i].dispatch).toJSON().slice(0, 10) // get only month, date, and year
            if (mdyOfCrime in dateOfArrest && mdyOfCrime in dateofCrime) {
                dateofCrime[mdyOfCrime] += 1;
            }
            else if (mdyOfCrime in dateOfArrest && !(mdyOfCrime in dateofCrime)) {
                dateofCrime[mdyOfCrime] = 1;
            }
        }
    }

    // Line chart must exist before updating 
    if (linechart) {

        // Clear old data
        while (linechartData.getNumberOfRows() > 0) {
            linechartData.removeRow(0)
        }

        // Add updated data
        for (let date in dateOfArrest) {
            linechartData.addRow([new Date(date), dateOfArrest[date]])
            // linechartData.addRow([date, dateOfArrest[date]])

        }

        var options = {
            hAxis: {
                direction:1, slantedText:true, slantedTextAngle:40
            },
            vAxis: {
                title: 'Frequency'
            },
            legend: { position: 'left' },
            title: 'Arrest Freqency by Date',
            width: 600,
            height: 500,
            fontSize: 16
        };

        linechart.draw(linechartData, options);
    }

}
