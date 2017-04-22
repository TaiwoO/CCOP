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
	"bFilter": false,
	"bPaginate": false,
	"bLengthChange": false,
	"bInfo": false,
	"scroller": true,
	"columns": [
	    { "title": "Offense", "data" : "description" },
	    { "title": "Dispatch Time", "data" : "dispatch" },
	    { "title": "Address", "data" : "street" }
	]
    });
    arrestTable = $("#arresttable").DataTable({
	"deferRender": true,
	"bFilter": false,
	"bPaginate": false,
	"bLengthChange": false,
	"bInfo": false,
	"scroller": true,
	"columns": [
	    { "title": "Time", "data" : "date" },
	    { "title": "Address", "data" : "street" },
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
    crimeTable.draw();
    arrestTable.draw();
}
