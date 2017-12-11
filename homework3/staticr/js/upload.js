
	

$("#hideform").hide()


//AJAX for uploading
$('#post-form').on('submit', function(e){
	e.preventDefault();

	$.ajax({
		url : "/upload/", // the endpoint
		type : "POST", // http method
		data : { 
			jobname : $('#id_name').val(), 
			file1 : $('#id_file1').val(),
			file2 : $('#id_file2').val(),
			file3 : $('#id_file3').val() 
		
		}, // data sent with the post request*/

		success : function(json) {
			$('#id_name').val(''); // remove the value from the input
			$('#id_file1').val('');
			$('#id_file2').val('');
			$('#id_file3').val('');
			//console.log(json); // log the returned json to the console
			$("#job_list").prepend("\
									<tbody id='job-"+json.id+"'><tr>\
									<td>"+json.id+"</td>\
									<td>"+json.jobname+"</td>\
									<td>"+json.created_time+"</td>\
									<td><a id='execute-job-"+json.id+"' class=\"btn btn-primary btn-xs btn-info\">Execute</a></td>\
									<td><a id='delete-job-"+json.id+"' class=\"btn btn-primary btn-xs btn-danger\">Delete</a></td>\
									</tr></tbody>\
									");
									//<td><span id='status-job-"+json.id+"' class=\"label label-primary\">"+json.status+"</span></td>\
			//clear error message
			$('#g_name').html("");
			$('#gg_name').removeClass("has-error");	
			$('#g_file1').html("");
			$('#gg_file1').removeClass("has-error");	
			$('#g_file2').html("");
			$('#gg_file2').removeClass("has-error");	
			$('#g_file3').html("");
			$('#gg_file3').removeClass("has-error");
			$('#results').html("\
								<div class=\"alert alert-dismissible alert-info\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Wow!</strong> <a href=\"#\" class=\"alert-link\"> Add job successfully!\
								</div>\
								").delay(5000).fadeOut(400);
			$("#hideform").fadeToggle();
		},

		// handle a non-successful response
		error : function(xhr,errmsg,err) {
			$('#results').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> All fields are required.\
								</div>\
								").delay(5000).fadeOut(400);
			var info = JSON.parse(xhr.responseText)
			if (info.jobname){
				$('#g_name').html("<span class=\"label label-danger\">"+info.jobname+"</span>");
				$('#gg_name').addClass("has-error");				
			}else{
				$('#g_name').html("");
				$('#gg_name').removeClass("has-error");	
			}			
			if (info.file1){			
				$('#g_file1').html("<span class=\"label label-danger\">"+info.file1+"</span>");	
				$('#gg_file1').addClass("has-error");	
			}else{
				$('#g_file1').html("");
				$('#gg_file1').removeClass("has-error");	
			}							
			if (info.file2){						
				$('#g_file2').html("<span class=\"label label-danger\">"+info.file2+"</span>");
				$('#gg_file2').addClass("has-error");	
			}else{
				$('#g_file2').html("");
				$('#gg_file2').removeClass("has-error");	
			}						
			if (info.file3){						
				$('#g_file3').html("<span class=\"label label-danger\">"+info.file3+"</span>");
				$('#gg_file3').addClass("has-error");	
			}else{
				$('#g_file3').html("");
				$('#gg_file3').removeClass("has-error");	
			}	
			

				
		}
	});
	
});

//form 

$("#newjob").click(function(){
  $("#hideform").fadeToggle();
  $('#results').html("");
  
   /* $('#hideform').html("\
		<div class='row'>\
			<div class='col-lg-12 col-md-12 col-sm-12'>	\
				<form action'/upload/' method='post' enctype='multipart/form-data' class='form-horizontal' id='post-form'>\
					<div class='jumbotron'>\
					<fieldset>\
						<legend>Create a new Job</legend>\
						<div class='form-group' id='gg_name'>\
						  <label for='jobname' class='col-lg-2 control-label'>Job name</label>\
						  <div class='col-lg-10'> \
							<div id='g_name'></div>\
							<input type='text' class='form-control' id='id_name' name='name'  placeholder='Job name'>\
						  </div>\
						</div>\
						<div class='form-group ' id='gg_file1'>\
						  <label for='textArea' class='col-lg-2 control-label'>Mapper.py</label>\
						  <div class='col-lg-10 '>\
							<div id='g_file1'></div>\
							<textarea class='form-control' rows='3' id='id_file1'></textarea>\
						  </div>\
						</div>\
						<div class='form-group' id='gg_file2'>\
						  <label for='textArea' class='col-lg-2 control-label'>Reducer.py</label>\
						  <div class='col-lg-10'>\
							<div id='g_file2'></div>\
							<textarea class='form-control' rows='3' id='id_file2'></textarea>\
						  </div>\
						</div>\
						<div class='form-group' id='gg_file3'>\
						  <label for='textArea' class='col-lg-2 control-label'>Input file</label>\
						  <div class='col-lg-10'>\
							<div id='g_file3'></div>\
							<textarea class='form-control' rows='3' id='id_file3'></textarea>\
						  </div>\
						</div>\
						<div class='form-group'>\
						  <div class='col-lg-10 col-lg-offset-2'>\
							<button type='submit' class='btn btn-default btn-primary'>Submit</button>\
							<button type='reset' class='btn btn-default'>Reset</button>\
						  </div>\
						</div>\
					</fieldset>\
					</div>\
				</form>\
			</div>\
		</div>"
    );*/
  
  
});


// delete
$("#job_list").on('click', 'a[id^=delete-job-]', function(){
	var job_primary_key = $(this).attr('id').split('-')[2];
	//console.log(job_primary_key) // sanity check
	delete_post(job_primary_key);
});

// AJAX for deleting
function delete_post(job_primary_key){
	if (confirm('Are you sure you want to remove this job?')==true){
		$.ajax({
			url : "/delete/"+job_primary_key, // the endpoint
			type : "DELETE", // http method
			data : { jobpk : job_primary_key }, // data sent with the delete request
			success : function(json) {
				// hide the post
			  $('#job-'+job_primary_key).fadeOut(); // hide the post on success
			  //console.log("post deletion successful");
			},

			error : function(xhr,errmsg,err) {
				// Show an error
				$('#results').html("<div class='alert-box alert radius' data-alert>"+
				"Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
				//console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			}
		});
	} else {
		return false;
	}
};


//get status
function get_status(job_primary_key){
	$.ajax({
			url : "/status/", // the endpoint
			type : "GET", // http method
			data : { id : job_primary_key }, // data sent with the delete request
			success : function(json) {
				// hide the post
			    //$('#execute-job-'+job_primary_key).addClass("btn-warning"); // hide the post on success
			    //console.log(json.result);
			  
				$('#status').html("\
								<fieldset>\
								<div class='jumbotron'><legend>Result</legend>\
								<textarea class='form-control' rows='10' id='textArea'>"+json.result+"</textarea></div></fieldset>\
								").delay(5000).fadeOut(400);
								
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#results').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot get the status.\
								</div>\
								").delay(5000).fadeOut(400);			
			}
		});
};


// execute
$("#job_list").on('click', 'a[id^=execute-job-]', function(){
	var job_primary_key = $(this).attr('id').split('-')[2];
	//console.log(job_primary_key) // sanity check
	execute(job_primary_key);
});

// AJAX for execute
function execute(job_primary_key){
	if (confirm('Are you sure you want to execute this job?')==true){
		
		//$('#status-job-'+job_primary_key).text("RUNNING"); // hide the post on success
		
		$.ajax({
			url : "/execute/", // the endpoint
			type : "GET", // http method
			data : { id : job_primary_key }, // data sent with the delete request
			success : function(json) {
				// hide the post
			  //$('#execute-job-'+job_primary_key).addClass("btn-warning"); // hide the post on success
			  //console.log(json.result);
			  
			$('#results').html("\
								<div class=\"alert alert-dismissible alert-info\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>YA!</strong> <a href=\"#\" class=\"alert-link\"> Execute job successfully!\
								</div>\
								").delay(5000).fadeOut(400);
			get_status(job_primary_key);
			  
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#results').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot execute the job.\
								</div>\
								").delay(5000).fadeOut(400);		
			}
		});
	} else {
		return false;
	}
};

//loading

$(document).ajaxStart(function(){
  $("#loading_msg").html("<div class=\"progress progress-striped active\">\
				<div class=\"progress-bar\" style=\"width: 100%\"></div></div>")
});
$(document).ajaxStop(function(){
  $("#loading_msg").html("");
}); 

