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
            width: 500,
            height: 500
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

            var options = {
                title: 'Crime types',
                pieHole: 0.4,
                width: 500,
                height: 500
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
    linechartData.addColumn('string', 'Arrest')
    linechartData.addColumn('number', 'Arrests');
    // linechartData.addColumn('number', 'The Avengers');
    // linechartData.addColumn('number', 'Transformers: Age of Extinction');
    // linechartData.addRows([
    //     [1, 37.8, 80.8, 41.8],
    //     [2, 30.9, 69.5, 32.4],
    //     [3, 25.4, 57, 25.7],
    //     [4, 11.7, 18.8, 10.5],
    //     [5, 11.9, 17.6, 10.4],
    //     [6, 8.8, 13.6, 7.7],
    //     [7, 7.6, 12.3, 9.6],
    //     [8, 12.3, 29.2, 10.6],
    //     [9, 16.9, 42.9, 14.8],
    //     [10, 12.8, 30.9, 11.6],
    //     [11, 5.3, 7.9, 4.7],
    //     [12, 6.6, 8.4, 5.2],
    //     [13, 4.8, 6.3, 3.6],
    //     [14, 4.2, 6.2, 3.4]
    // ]);

    var options = {
        hAxis: {
            title: 'Dates'
        },
        vAxis: {
            title: 'Frequency'
        },

        title: 'Arrest Frequency by Date',

        width: 600,
        height: 400
    };

    // linechart = new google.visualization.Histogram(document.getElementById('histogram'));

    linechart = new google.visualization.LineChart(document.getElementById('histogram'));
    //linechart.draw(linechartData, options);

    if (window.arrestJSON)
        updateLineChart(window.arrestJSON)

}


function updateLineChart(arrests) {
    
    var dateOfArrest = {};
    var totalArrests = arrests.length;
    
    console.log(totalArrests)
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

    // Line chart must exist before updating 
    if (linechart) {

        // Clear old data
        while (linechartData.getNumberOfRows() > 0) {
            linechartData.removeRow(0)
        }

        // Add updated data
        for (let date in dateOfArrest) {
            linechartData.addRow([date, dateOfArrest[date]])
        }

        var options = {
            hAxis: {
                title: 'Dates'
            },
            vAxis: {
                title: 'Frequency'
            },

            title: 'Arrest Freqency by Date',

            width: 600,
            height: 400
        };

        linechart.draw(linechartData, options);
    }

}
