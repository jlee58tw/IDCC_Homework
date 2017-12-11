

//get concert
function get_concert(pk){
	$.ajax({
			url : "/api/getConcert/", // the endpoint
			type : "GET", // http method
			//data : { id : pk }, // data sent with the delete request
			success : function(json) {
				// hide the post
			    //$('#execute-job-'+job_primary_key).addClass("btn-warning"); // hide the post on success
			    //console.log(json.result);
				
				var res = ""
				
				for (i = 0; i < json.data.length; i++) { 
					res += "\
									<div class='content_box col-xs-12 col-sm-6 col-md-4'>\
										<div class='panel panel-default'>\
											  <div class='panel-heading list-group-item'>\
													<h4>"+json.data[i].title+"</h4>\
											  </div>\
											  <div class='list-group-item'><a href='/detail/"+json.data[i].id+"'><img class='img-thumbnail' src='http://i.ytimg.com/vi/"+json.data[i].url_pic+"/0.jpg'></a></div>\
											  <div class='list-group-item'><i class='fa fa-calendar fa-fw'></i>&nbsp;時間："+json.data[i].time+"</div>\
											  <a id ='L"+json.data[i].index+"' onclick='toggleloc("+json.data[i].index+")' class='list-group-item' ><i class='fa fa-map-marker fa-fw'></i>&nbsp;地點："+json.data[i].locationName+"</a>\
											  <a id ='A"+json.data[i].index+"' onclick='toggleloc("+json.data[i].index+")' class='address list-group-item' ><i class='fa fa-map-marker fa-fw'></i>&nbsp;地址："+json.data[i].location+ "</a>\
											  <a class='list-group-item' target='_blank' href='"+json.data[i].web+"'><i class='fa fa-user fa-fw'></i>&nbsp;售票網站："+json.data[i].webName+"<span class='badge'>"+json.data[i].onsales+"</span></a>\
										</div>\
									</div>\
								";
				}
				$('#result').html("<div class='row _container'>"+res+"</div>");
				$('.address').hide();

				var $container = $('._container').masonry({        
					itemSelector: '.content_box',
				});
				$container.imagesLoaded( function() {
				  $container.masonry();
				});

								
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#result').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot get the data.\
								</div>\
								");			
			}
		});
};

function goto_page(p){
	setCookie('ppt_page',p);
	get_ptt();
}

//
function get_ptt(){
	
	p = getCookie('ppt_page');
	if (!p){
		p = 1;
	}
		//alertify.success(p);
	
	$.ajax({
			url : "/api/getPTT/", // the endpoint
			type : "GET", // http method
			data : { page : p }, 
			success : function(json) {
				// hide the post
			    //$('#execute-job-'+job_primary_key).addClass("btn-warning"); // hide the post on success
			    //console.log(json.result);
				var s,e,pagination,singer,follow;
				var last_page = Math.floor(json.count/20);
				p = parseInt(p);

				if(p==1){
					pagination = "<ul class='pagination pagination-sm btn'>\
										<li class='disabled'><a onclick='goto_page(1)'>&laquo;</a></li>"
				}else{
					pagination = "<ul class='pagination pagination-sm btn'>\
										<li><a onclick='goto_page(1)'>&laquo;</a></li>"
				}
				if( p < 5){
					s = 1;e = 10;
				}
				else if ( (p+5) > last_page){
					e = last_page; s = last_page - 9;
				}
				else{
					s = p-4;e = p + 5;
				}

				for (i = s; i <= e; i++) { 
					if (i==p){
						if(i<10){i='0'+i}
						pagination = pagination + "<li class='active '><a onclick='goto_page("+i+")'>"+i+"</a></li>"
					}else{
						if(i<10){i='0'+i}
						pagination = pagination + "<li><a onclick='goto_page("+i+")'>"+i+"</a></li>"
					}
				}		
				
				if(p==last_page){
					pagination = pagination + "<li class='disabled'><a onclick='goto_page("+ last_page +")'>&raquo;</a></li>\
												</ul>";
				}else{
					pagination = pagination + "<li><a onclick='goto_page("+ last_page +")'>&raquo;</a></li>\
												</ul>";
				}
				
				pagination = pagination +  "<span class='label label-primary'>第"+p+"頁，共"+last_page+"頁</span>"

				var res = "\
								<table class='table table-striped table-hover'>\
								  <thead>\
								    <tr>\
								      <th>編號</th>\
								      <th>標題</th>\
								      <th>分類</th>\
									  <th>訂閱</th>\
								      <th>作者</th>\
								      <th>發文時間</th>\
								    </tr>\
								  </thead><tbody>\
							"
				for (i = 0; i < json.data.length; i++) { 
				
					if(json.data[i].singer){
						singer = json.data[i].singer;
						id = json.data[i].singerid;
						if(json.subsinger){
						
							follow =  "<a onclick='add_sub("+id+")' id='sub"+id+"' class='btn btn-info btn-xs'>訂閱分類</a>";
						
							for (j = 0; j < json.subsinger.length; j++) {
								if(json.subsinger[j].singerid == id){
									follow =  "<a class='btn btn-success btn-xs disabled'>已經訂閱</a> ";
									break;
								}
							}
						}else{
							follow = "<a class='btn btn-info btn-xs disabled'>無法訂閱</a>";
						}
						
					}else{
						singer = '未分類';
						follow = "<a class='btn btn-default btn-xs disabled'>無法訂閱</a>";
					}
				
					res += "\
								  \
								    <tr>\
								      <td>"+json.data[i].postid+"</td>\
								      <td><a href='"+json.data[i].url+"' style=text-decoration:none;color:#000000;>"+json.data[i].title+"</a></td>\
								      <td>"+singer+"</td>\
									  <td>"+follow+"</td>\
								      <td>"+json.data[i].author+"</td>\
								      <td>"+json.data[i].time+"</td>\
								    </tr>\
								";
				}

				res = res + "</tbody></table>"

				$('#result').html("<div class='row _container'>"+res+"</div>");
				$('.pagination').html("<div class='row _container'>"+pagination+"</div>");
				//$('.address').hide();
				//$('._container').masonry({        
				//	itemSelector: '.content_box',
				//});

								
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#result').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\">Cannot get the data.\
								</div>\
								");			
			}
		});
};

//
function get_pttnum(p){
	$.ajax({
			url : "/api/getPTTnum/", // the endpoint
			type : "GET", // http method
			success : function(json) {
				
			var num = json.num;

			var res = "<ul class='pagination'>\
						  <li class='disabled'><a href='#'>&laquo;</a></li>"
			for (i = 1; i <= 10; i++) { 
				res = res + "<li><a onclick='get_ptt("+i+")'>"+i+"</a></li>"

			}						  
					res = res + "<li><a href='#'>&raquo;</a></li>\
						</ul>\
						";

				$('#bar').html("<div class='row _container'>"+res+num+"</div>");
				//$('.address').hide();
				//$('._container').masonry({        
				//	itemSelector: '.content_box',
				//});

								
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#bar').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot get the data.\
								</div>\
								");			
			}
		});
};

//
function add_sub(id){
	$.ajax({
			url : "/api/addSubscribe/", // the endpoint
			type : "GET", // http method
			data : { singerid : id },
			success : function(json) {
			
				var resid = json.singerid;
				$('#add').html("<script>alertify.success('您已成功訂閱');</script>");
				$('#sub'+id).html("已經訂閱");
				$('#sub'+id).attr('class', "btn btn-success btn-xs disabled");
				
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#add').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot get the data.\
								</div>\
								");			
			}
		});
};

//
function get_sub(){
	$.ajax({
			url : "/api/getSubscribe/", // the endpoint
			type : "GET", // http method
			success : function(json) {
			
				var resid = json.singerid;
				
				var res = "\
								<table class='table table-striped table-hover'>\
								  <thead>\
								    <tr>\
									  <th>編號</th>\
								      <th>類別</th>\
								      <th>時間</th>\
									  <th>取消訂閱</th>\
								    </tr>\
								  </thead><tbody>\
							"
				for (i = 0; i < json.data.length; i++) { 
							
					res += "\
								  \
								    <tr id='sub_"+json.data[i].singerid+"'>\
								      <td>"+(i+1)+"</td>\
									  <td>"+json.data[i].singername+"</td>\
								      <td>"+json.data[i].time+"</td>\
									  <td><a onclick='del_sub("+json.data[i].singerid+")' id='del_"+json.data[i].singerid+"' class='btn btn-danger btn-xs'>取消訂閱</a></td>\
								    </tr>\
								";
				}

				res = res + "</tbody></table>"
				
				if(json.data.length == 0){
					$('#result').html("<div class='row _container'>目前沒有訂閱任何內容</div>");
				}else{
					$('#result').html("<div class='row _container'>"+res+"</div>");
				}

				

				
			},
			error : function(xhr,errmsg,err) {
				// Show an error
				$('#add').html("\
								<div class=\"alert alert-dismissible alert-danger\">\
								  <button type='button' class='close' data-dismiss='alert'>X</button>\
								  <strong>Oops!</strong> <a href=\"#\" class=\"alert-link\"> Cannot get the data.\
								</div>\
								");			
			}
		});
};

//
function del_sub(id){
	if (confirm('您確定要取消嘛?')==true){
		$.ajax({
			url : "/api/delSubscribe/"+id, // the endpoint
			type : "DELETE", // http method
			data : { id : id }, // data sent with the delete request
			success : function(json) {
				// hide the post
			  
			  $('#sub_'+id).html("<script>alertify.success('您已取消訂閱');</script>");
			  $('#sub_'+id).fadeOut(); // hide the post on success
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

function setCookie(name,value)
{
    var Days = 30; 
    var exp  = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}

function getCookie(name)       
{
    var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
     if(arr != null) return unescape(arr[2]); return null;
}

function toggleloc(loc){
	
	$("#A"+loc).toggle();
	$("#L"+loc).toggle();
	
};