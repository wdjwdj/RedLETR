<?php
$title = '';
//Check if there are any files ready for upload
if(isset($_FILES['uploaded_dict_files']))
{
	//For each file get the $key so you can check them by their key value
	foreach($_FILES['uploaded_dict_files']['name'] as $key => $value)
	{
			//If the file was uploaded successful and there is no error
		if(is_uploaded_file($_FILES['uploaded_dict_files']['tmp_name'][$key]) && $_FILES['uploaded_dict_files']['error'][$key] == 0)
{

			//Create an unique name for the file using the current timestamp, an random number and the filename
			$name = $_FILES['uploaded_dict_files']['name'][$key];
			$ext = end(explode(".", $name));
			if ($ext == 'csv') {
				$title = time().rand(0,999);
				$filename = $title.".".$ext;
				$today = date("m.d.y.G.i.s");
				$filename = $today.".".$ext;

				//Check if the file was moved
				if(move_uploaded_file($_FILES['uploaded_dict_files']['tmp_name'][$key], 'uploads/dictionary/'. $filename))
				{
					echo 'The file ' . $_FILES['uploaded_dict_files']['name'][$key].' was uploaded successful <br/>';
				}
				else
				{
					echo move_uploaded_file($_FILES['uploaded_dict_files']['tmp_name'][$key], 'uploads/dictionary/'. $filename);
					echo 'The file was not moved.';
				}
			}
			else {
				echo 'Cannot upload file other than csv.';
			}

}
		else
{
			echo 'The file was not uploaded.';
}
	}
}

//Check if there are any files ready for upload
if(isset($_FILES['uploaded_data_files']))
{
	//For each file get the $key so you can check them by their key value
	foreach($_FILES['uploaded_data_files']['name'] as $key => $value)
	{

		//If the file was uploaded successful and there is no error
		if(is_uploaded_file($_FILES['uploaded_data_files']['tmp_name'][$key]) && $_FILES['uploaded_data_files']['error'][$key] == 0)
{

			//Create an unique name for the file using the current timestamp, an random number and the filename
			$dname = $_FILES['uploaded_data_files']['name'][$key];
			$dext = end(explode(".", $dname));
			if ($dext == 'csv') {
				if ($_POST['txtdictionary'] == '') {
					echo 'Please select dictionary file before uploading data file.';
				}
				else {
					$fname = $_POST['txtdictionary']."_".time().rand(0,999).".".$dext;

					//Check if the file was moved
					if(move_uploaded_file($_FILES['uploaded_data_files']['tmp_name'][$key], 'uploads/data/'. $fname))
					{
						echo 'The file ' . $_FILES['uploaded_data_files']['name'][$key].' was uploaded successful <br/>';
					}
					else
					{
						echo move_uploaded_file($_FILES['uploaded_data_files']['tmp_name'][$key], 'uploads/data/'. $fname);
						echo 'The file was not moved.';
					}
				}
			}
			else {
				echo 'Cannot upload file other than csv.';
			}

}
		else
{
			echo 'The file was not uploaded.';
}
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" href="style.css" media="screen, projection"/>
	<link rel="STYLESHEET" type="text/css" href="codebase/dhtmlx.css">
	<script src="codebase/dhtmlx.js"></script>
	<script src="codebase/csv2array.js"></script>
	<script src="validate.js"></script>
	<script src="http://code.jquery.com/jquery-1.8.2.js"></script>

	<script src="http://jquery-csv.googlecode.com/git/src/jquery.csv.js"></script>
	<script src="redletr_helper_functions.js"></script>
	<style>
	.upload_box
		{
		margin: 2px;
		border: 1px solid blue;
		}
	</style>

  <style>
     /*these styles allows dhtmlxLayout to work in the Full Screen mode in different browsers correctly*/
  html, body {
  width: 100%;
  height: 100%;
  margin: 0px;
  overflow: hidden;
  background-color: white;
  }
  #container {
  width: 100%;
  height: 100%;
  background-color: black;
  border: 1px solid black;
  color: white; /* for error messages, etc. */
  }
  </style>
  </head>
  

<script type="text/javascript">

	//define global variables here
	var csvdatafile_grid ;
	var csv_data_grid;
	var redcap_datadict = new Object();
	var main_layout;

function doOnLoad() {
		main_layout = new dhtmlXLayoutObject(document.body, '4I');
		//made this global...
		header_rgn  = main_layout.cells('a');
		header_rgn.setHeight('150');
		header_rgn.attachObject('header_box');
		header_rgn.setText('');
		header_rgn.hideHeader();
		header_menu = header_rgn.attachToolbar();
		
		/* attach buttons here */
		header_menu.addButton('help',1,'Help');
		header_menu.addButton('about',2,'About');
		header_menu.addButton('gen_grid_stats',3,'Generate Grid Stats');
		header_menu.addButton('validate',4,'Validate Grid Data');
		header_menu.addButton('hide_data_dict',5,'Hide Data Dict');
		
		
		/*Define events for each button */
		function getId() {
		    var id = sel.options[sel.selectedIndex].value;
		return id;
		}
		function show() {
		    var id = getId();
		toolbar.showItem(id);
		}
		function hide() {
		    var id = getId();
		toolbar.hideItem(id);
		}
		function isVisible() {
		    var id = getId();
		alert(toolbar.isVisible(id));
		}
		function updateList() {
		    sel.options.length = 0;

		toolbar.forEachItem(function(itemId) {
		if (toolbar.getType(itemId) == "button") {
		    sel.options.add(new Option(itemId, itemId));
		    }
		});
		
		}
		
		header_menu.attachEvent("onClick", function(id){   
		         alert("Button "+id+" was clicked");    
		             });
		
		
		datadict_rgn = main_layout.cells('b');
		datadict_rgn.attachObject('redcap_datadict_div');
		datadict_rgn.setText('RedCap Data Dictionary');
		
		csvdatafile_rgn = main_layout.cells('d');
		csvdatafile_rgn.attachObject('csv_datafile_div');
		csvdatafile_rgn.setText('CSV Data File');
		
		main_layout.cells('c').attachObject('upload_ctrls');
		main_layout.cells('c').setWidth('200');
					}

	/* This object will contain all of the data and parameters associated with the grid that holds the redcap_datadict object...
	To make the grid look nice certain properties need to be configured such as column sorting, alignment, etc... these will be computed
	and then set via the object
	properties such as column alignment, column names, sorting, etc are configured in the helper functions
	dhtmlx configures the grid using a comma separates list such as  center,center,center,center
	*/
      function get_csvdata() {

      // retrieve data--- first get the data dictionary for the data set
	datadict_text =  document.getElementById("textbox").value;	
	redcap_datadict.raw_csv_data = document.getElementById("textbox").value;
      // convert data to array
       convert_csvstring_to_object( redcap_datadict  );


		datadict_grid = new dhtmlXGridObject('datadict_gridbox');
		datadict_grid.selMultiRows = true;
		datadict_grid.imgURL = "codebase/imgs/icons_greenfolders/";

		/* Now set the alignment, widths, header, etc.. for the current datagrid */
		datadict_grid.setHeader(redcap_datadict.Header);
		datadict_grid.setInitWidths(redcap_datadict.InitWidths );
		datadict_grid.setColAlign(redcap_datadict.ColAlign);
		datadict_grid.setColTypes(redcap_datadict.ColTypes);
		datadict_grid.setColSorting(redcap_datadict.ColSorting);

		datadict_grid.setSkin("dhx_skyblue");
		datadict_grid.init();

		add_data_to_grid(datadict_grid, redcap_datadict)	;
		datadict_grid.attachHeader("#text_filter,#select_filter,#numeric_filter");

	/* Now loading and populating the data for the CSV data */

	  var gd = document.getElementById("tbox").value;
	  datafile_csv = new Object();
	  datafile_csv.raw_csv_data = gd;
	  convert_csvstring_to_object( datafile_csv  );


		csvdatafile_grid = new dhtmlXGridObject('data_gridbox');
		csvdatafile_grid.selMultiRows = true;
		csvdatafile_grid.imgURL = "codebase/imgs/icons_greenfolders/";

		/*Set Grid configuration parameters */
		csvdatafile_grid.setHeader(datafile_csv.Header);
		csvdatafile_grid.setInitWidths(datafile_csv.InitWidths);
		csvdatafile_grid.setColAlign(datafile_csv.ColAlign);
		csvdatafile_grid.setColTypes(datafile_csv.ColTypes);
		csvdatafile_grid.setColSorting(datafile_csv.ColSorting);

		csvdatafile_grid.init();
		csvdatafile_grid.setSkin("dhx_skyblue");
		add_data_to_grid(csvdatafile_grid, datafile_csv)

	  }

   /* to replace... but this function grabes the previously uploaded files used for the deo */
	$(document).ready(function(){
		$.get('list-files.php', function(result) {
			var flist =  $("#flist");
			var myArr = result.split(',');
			for (var i=0; i<myArr.length; i+=1) {
				flist.append($("<option></option>").val(myArr[i]).html(myArr[i] + '.csv'));
			}
		});

		$('#flist').change(function() {
			var str = "";
			$("select option:selected").each(function () {
				str += $(this).text();
    });
			var myArr = str.split('_');
			$.get('uploads/dictionary/' + myArr[0] + '.csv', function(result) {
					$('#textbox').val(result);
			});
			$.get('uploads/data/' + str, function(result) {
					$('#tbox').val(result);
			});

		});

	});

	</script>
</head>

<body onload="run_init_code();doOnLoad()">

<div id="header_box" style="border: 1px solid black">
<div style="float:left">
<h1><img src="red_envelope.jpg" height=80 style="margin:5px;float:left">Welcome to RED Lettr   </h1>
</div>

<div id="button_ctrls" style="border:1px solid black;float:left">
	<button name="help" value="help">Help</button><button name="about" value="about">About</button>
	<button id="grid_stats_button" onClick="grid_stats()"  >Generate Grid Stats</button>
	<button id="validate_button" onClick="validate_grid()" name="Validate">Validata Data Grid</button>
	<button id="hide_dict" onClick="hide_data_dict()" >Hide Dact Dict</button>
  </div>

<span id="data_stats_div" style="border: 1px solid black; width:300px; float:right">
Stats:
Number of elements in data dict:<br>
Number of rows in uploaded data file:<br>
Number of columsn in uploaded data dict:<br>
</span>
</div>



<script >

var grid_stats_obj = new Object();

function compute_basic_grid_stats()
	{
	
	grid_stats_obj.rows_in_csv =  csvdatafile_grid.getRowsNum();
	grid_stats_obj.cols_in_csv =  csvdatafile_grid.getColumnsNum();
	
	grid_stats_obj.redcap_datadict_variable_count = datadict_grid.getRowsNum();
	
	/*add export to CSV/Excel functions...*/
	
	}
	

function run_init_code()
	{
	/* move functions into here; can't add filters until the data is actually loaded*/
	}


function bobs_function(){
	box_visibility = $("#upload_file_box")[0];
	box_visibility.hidden? box_visibility.hidden= false : box_visibility.hidden = true
	}
</script>

<div id="upload_ctrls">

<div id="upload_file_box" class="upload_box">
<table style="padding: 0px; margin: 0px; border: 0px; width: 100%" border="0">
<tr><td style="text-align: left; width: 50%">
<div class="left_header">Upload Dictionary File:</div>
<div class="right_header">Upload Data File:</div>


<form action="upload.php" method="POST" enctype="multipart/form-data">
	<div class="input_holder">
		<input type="file" name="uploaded_dict_files[]" id="input_clone" />
	</div>
<!--	<input type="submit" value="add_files" />-->
</form>
</td>
<td style="text-align: left; width: 50%">
<form action="upload.php" method="POST" enctype="multipart/form-data">
	<div class="holder_input">
		<input type="file" name="uploaded_data_files[]" id="clone_input" />
		<input type="hidden" name="txtdictionary" id="txtdict" value="<?php echo $title; ?>">
	</div>
<!--	<input type="submit" value="add_files" />-->
</form>
</td>
</tr>
<table>
</div>


<div>
<table style="padding: 0px; margin: 0px; border: 0px; width: 100%" border="0">
<tr><td colspan="2" style="text-align: left; width: 100%">
<div id="files-list">
<select id="flist"><option value="">Select from uploaded files</option></select>
<input type="button" value="Get Array from CSV" onclick="get_csvdata();">
</div>
<!-- this is a weird way to store data and will be removed in the near future...
currently we are saving read in input into textboxes which seems a bit odd
-->
</div>

<textarea rows="40" cols="400" id="textbox" style="display:none"></textarea>
<textarea rows="40" cols="400" id="xmlbox" style="display: none"></textarea>
<textarea rows="40" cols="400" id="databox" style="display: none"></textarea>

<textarea rows="40" cols="400" id="tbox" style="display: none"></textarea>
<textarea rows="40" cols="400" id="xbox" style="display: none"></textarea>
<textarea rows="40" cols="400" id="dbox" style="display: none"></textarea>




<div id="redcap_datadict_div">
REDCap Data Dictionary:
<div id="datadict_gridbox" width="100%" height="250px" style="background-color:white;"></div>
</div>

<div id="csv_datafile_div">
<div id="data_gridbox" width="100%" height="250px" style="background-color:white;"></div>
</div>


</body>
</html>
