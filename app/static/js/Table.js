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
*/
function initTables(){
    crimeTable = $("#crimetable").DataTable({
	"deferRender": true,
	"bFilter": false,
	"bPaginate": false,
	"bLengthChange": false,
	"bInfo": false,
	"scroller": true
    });
    arrestTable = $("#arresttable").DataTable({
	"deferRender": true,
	"bFilter": false,
	"bPaginate": false,
	"bLengthChange": false,
	"bInfo": false,
	"scroller": true
    });
    
};

//clear old rows and add new ones based on crime/arrest data passed in
function updateTables(crimes, arrests){
    var crimeRow;
    var arrestRow;

    

}
