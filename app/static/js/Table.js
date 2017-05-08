/*
  File containing implementation of tabular view using DataTables
*/

var crimeTable;
var arrestTable;

/*
  initiate tables
  more info about options at:
  http://legacy.datatables.net/usage/features
  https://datatables.net/reference/option/

  columns parameter specifies column headers, data specifies its key within whatever data array you pass into updateTables
*/
function initTables(){
    crimeTable = $("#crimetable").DataTable({
	"deferRender": true,
	"searching": false,
	"paging": true,
	"lengthChange": false,
	"info": false,
	"scroller": true,
	"scrollY": 200,
	"scrollCollapse": true,
	"processing": true,
	"autoWidth": false,
	"scrollX": true,
	"columns": [
	    { "title": "Time", "data" : "dispatch" },
	    { "title": "City", "data" : "city" },
	    { "title": "Offense", "data" : "description" }
	]
    });
    arrestTable = $("#arresttable").DataTable({
	"deferRender": true,
	"searching": false,
	"paging": true,
	"lengthChange": false,
	"info": false,
	"scroller": true,
	"scrollY": 200,
	"scrollCollapse": true,
	"processing": true,
	"autoWidth": false,
	"scrollX": true,
	"columns": [
	    { "title": "Time", "data" : "date" },
	    { "title": "City", "data" : "city" },
	    { "title": "Offense", "data" : "offense" }
	]
    });
};

//clear old rows and add new ones based on crime/arrest data passed in
//this function ASSUMES (probably bad) that the tables exist when called
function updateTables(crimes, arrests){
    crimeTable.clear();
    arrestTable.clear();
    crimeTable.rows.add(crimes);
    arrestTable.rows.add(arrests);
    //crimeTable.ajax.url(crimes).load();
    //arrestTable.ajax.url(arrests).load();
    crimeTable.draw();
    arrestTable.draw();
    //console.log(crimeTable.data().count());
    //console.log(arrestTable.data().count());
}

//function for highlighting selected marker row in table
//params: table name, row id
//table name: use "crime" or "arrest"
//id should be proportionate to indices in whatever data arrays were used. [0 - CRIME/ARREST_MAX)
function highlightRow(name, id){
    //console.log("marker clicked. " + name + " " + id);
    if(name == "crime"){
	crimeTable.row(id).scrollTo(false);
    }else if(name == "arrest"){
	arrestTable.row(id).scrollTo(false);
    }
}
