function isNull(input){
  return input==null || 
    input=="" || 
    input<0 ||
    input=='NA' ||
    input=='na' ||
    input=='Na' ||
    input=='NaN' ||
    input=='none' ||
    input=='999'
}


// Yanhui's codes are from here

//	bool isBoolean(input) Returns true if input is either “true” or “false”

function isBoolean(input)
{
	return input=="true"||input=="false"
	       || input == "TRUE" || input == "FALSE"
}



//	bool isYesNo(input)	Returns true if input is either “yes” or “no”

function isYesNo(input)
{
	return input=="yes" || input=="no"
		|| input=="YES" || input=="NO"

}


//	bool correctYesNo(input)	Returns true if yes and false if no.

function correctYesNo(input)
{
	if(input == "yes" || input == "YES")
		return true;
	else if(input == "no" || input == "NO")
		return false;
		
}



function isInteger(input) {
  if((parseFloat(input) == parseInt(input)) && !isNaN(input)){
      return true;
  } else {
      return false;
  }

}

function isNumber(input) {
  return (isInteger(input) && input > 0);

}

function withinRange(input, min, max) {
     return (input > min && input <= max);   
}

function isIntegerWithinRange(input, min, max) {
  return (isInteger(input) && withinRange(input, min, max));

}






function validate_grid() {

	var col_dic = new Array();
	datadict_grid.forEachRow(function (id) {
		var dict_col = datadict_grid.cells(id, 0).getValue();
		if (dict_col != "") {
		    col_dic.push(dict_col)
		};
	});

	var  cols_in_csv  = csvdatafile_grid.getColumnsNum();

	for (var i = 0; i < cols_in_csv; i++) { 
			var col_id = csvdatafile_grid.getColumnLabel(i); 
			var col_index = col_dic.indexOf(col_id);
			if (col_index == -1) {  
				csvdatafile_grid.forEachRow(function (id) {     
					csvdatafile_grid.setCellTextStyle(id, i, "background-color: grey");
				});
			}
			else {
				csvdatafile_grid.forEachRow(function (id) {
					var cell_value=csvdatafile_grid.cells(id, i).getValue();
					//validation for NULL
					if (isNull(cell_value)){
						csvdatafile_grid.setCellTextStyle(id, i, "background-color: orange");
					}
					//ADD YOUR FUNCTIONS FOR OTHER TYPES OF VALIDATION


					// Yanhui's validation
					//	bool isBoolean(input) Returns true if input is either “true” or “false”
					if(isBoolean(cell_value)){
						csvdatafile_grid.setCellTextStyle(id,i,"background-color: green");
						//csvdatafile_grid.cells(id,i).setBgColor('green');

					}
					//	bool isYesNo(input)	Returns true if input is either “yes” or “no”
					if(isYesNo(cell_value)){
						csvdatafile_grid.setCellTextStyle(id,i,"background-color: green");
					}
					//	bool correctYesNo(input)	Returns true if yes and false if no.
					if(correctYesNo(cell_value)){
						csvdatafile_grid.setCellTextStyle(id,i,"background-color: green");
					}

					if(isInteger(cell_value)){
						csvdatafile_grid.setCellTextStyle(id,i,"background-color: green");
					}
					if(isNumber(cell_value)){
						csvdatafile_grid.setCellTextStyle(id,i,"background-color: green");
					}


				});
			}
	}
}



//Value parameter - required. All other parameters are optional.
function data_reg(value, sepVal, dayIdx, monthIdx, yearIdx) {
    try {
        //Change the below values to determine which format of date you wish to check. It is set to dd/mm/yyyy by default.
        var DayIndex = dayIdx !== undefined ? dayIdx : 0; 
        var MonthIndex = monthIdx !== undefined ? monthIdx : 0;
        var YearIndex = yearIdx !== undefined ? yearIdx : 0;
 
        value = value.replace(/-/g, "/").replace(/\./g, "/"); 
        var SplitValue = value.split(sepVal || "/");
        var OK = true;
        if (!(SplitValue[DayIndex].length == 1 || SplitValue[DayIndex].length == 2)) {
            OK = false;
        }
        if (OK && !(SplitValue[MonthIndex].length == 1 || SplitValue[MonthIndex].length == 2)) {
            OK = false;
        }
        if (OK && SplitValue[YearIndex].length != 4) {
            OK = false;
        }
        if (OK) {
            var Day = parseInt(SplitValue[DayIndex], 10);
            var Month = parseInt(SplitValue[MonthIndex], 10);
            var Year = parseInt(SplitValue[YearIndex], 10);
 
            if (OK = ((Year > 1900) && (Year < new Date().getFullYear()))) {
                if (OK = (Month <= 12 && Month > 0)) {

                    var LeapYear = (((Year % 4) == 0) && ((Year % 100) != 0) || ((Year % 400) == 0));   
                    
                    if(OK = Day > 0)
                    {
                        if (Month == 2) {  
                            OK = LeapYear ? Day <= 29 : Day <= 28;
                        } 
                        else {
                            if ((Month == 4) || (Month == 6) || (Month == 9) || (Month == 11)) {
                                OK = Day <= 30;
                            }
                            else {
                                OK = Day <= 31;
                            }
                        }
                    }
                }
            }
        }
        return OK;
    }
    catch (e) {
        return false;
    }
} 	


/**
 * @author Bob Chien
 */


/*
Datastatistics for grid
this function will take an array of values that were grabbed from the data grid... and then generate a 
count for the # of columns we have....

as is written.. generates the number of valid true/false responses in a column....

*/
function column_stats( gridcol_as_array )
{


for (var i=0;i<gridcol_as_array.length ;i++)
  { 
  	var y=0;
    var n=0;
    var none=0;
    
  	if (gridcol_as_array[i] == "None"|| gridcol_as_array[i] == "none")
  		{
  	none = none+1;
  		}
  	else if (gridcol_as_array[i] == "y" || gridcol_as_array[i] == "Y")
  		{
  	y = y+1;
  		}
  	else if (gridcol_as_array[i] == "n" || gridcol_as_array[i] =="N")
		{
  	n = n+1;
  	}
/*  	else 
  	count <<"Error!";
*/

  	}
  		var x="";
  	
		x=x + "The number is " + i + "<br>";
		document.getElementById("bob_demo").innerHTML=x;
	alert(x);
}


function get_dhxgrid_col_as_array( dhx_grid_id, col_idx)
	{
	/* Don't forget col_idx is 0 indexed...*/
	rows_in_grid = dhx_grid_id.getRowsNum();
	
	var col_array = new Array();
	
	for( var i=0; i< rows_in_grid; i++)
		{
		col_array[i] = dhx_grid_id.cellByIndex(i,col_idx).getValue();
		}
		
		
		
	return(col_array);
	
	}




