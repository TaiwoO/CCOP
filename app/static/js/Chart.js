//written by Taiwo
//will implement the Chart
// This file construct the charts of the application

function initCharts() {

    // Load the Visualization API and the corechart package.
    google.charts.load('current', { 'packages': ['corechart'] });

    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(drawPieChart);

    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(drawHistrogram);
}

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawPieChart(query) {
    
    //console.log(query);

    if(query === undefined)
        query = "";

    $.getJSON($SCRIPT_ROOT + "/crime/type" + query, {}, function (result) {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Crime Type')
        data.addColumn('number', 'frequency');

        var crimeTypes = result.crime_types;
        //console.log(crimeTypes)
        for (type in crimeTypes) {
            data.addRow([type, crimeTypes[type]]);
        }

        // Set chart options
        var options = {
            title: 'Crime types',
            pieHole: 0.4
        };
        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
    });
}


function drawHistrogram() {
    var data = google.visualization.arrayToDataTable([
        ['Dinosaur', 'Length'],
        ['Acrocanthosaurus (top-spined lizard)', 12.2],
        ['Albertosaurus (Alberta lizard)', 9.1],
        ['Allosaurus (other lizard)', 12.2],
        ['Apatosaurus (deceptive lizard)', 22.9],
        ['Archaeopteryx (ancient wing)', 0.9],
        ['Argentinosaurus (Argentina lizard)', 36.6],
        ['Baryonyx (heavy claws)', 9.1],
        ['Brachiosaurus (arm lizard)', 30.5],
        ['Ceratosaurus (horned lizard)', 6.1],
        ['Coelophysis (hollow form)', 2.7],
        ['Compsognathus (elegant jaw)', 0.9],
        ['Deinonychus (terrible claw)', 2.7],
        ['Diplodocus (double beam)', 27.1],
        ['Dromicelomimus (emu mimic)', 3.4],
        ['Gallimimus (fowl mimic)', 5.5],
        ['Mamenchisaurus (Mamenchi lizard)', 21.0],
        ['Megalosaurus (big lizard)', 7.9],
        ['Microvenator (small hunter)', 1.2],
        ['Ornithomimus (bird mimic)', 4.6],
        ['Oviraptor (egg robber)', 1.5],
        ['Plateosaurus (flat lizard)', 7.9],
        ['Sauronithoides (narrow-clawed lizard)', 2.0],
        ['Seismosaurus (tremor lizard)', 45.7],
        ['Spinosaurus (spiny lizard)', 12.2],
        ['Supersaurus (super lizard)', 30.5],
        ['Tyrannosaurus (tyrant lizard)', 15.2],
        ['Ultrasaurus (ultra lizard)', 30.5],
        ['Velociraptor (swift robber)', 1.8]]);

    var options = {
        title: 'Lengths of dinosaurs, in meters',
        legend: { position: 'none' },
    };

    var chart = new google.visualization.Histogram(document.getElementById('histogram'));
    chart.draw(data, options);
}
