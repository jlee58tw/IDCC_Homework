function tplawesome(e,t){
    res = e;
    for(var n=0;n<t.length;n++){
      res=res.replace(/\{\{(.*?)\}\}/g,function(e,r){
        return t[n][r]})
    }
    return res
  }
function resetVideoHeight() {
    $(".video").css("height", $("#results").width() * 9/16);
}

function init() {
    gapi.client.setApiKey("AIzaSyC_hBOQ4Z0gB3RU1Bpw32xAnUX-4gKAJ7c");
    gapi.client.load("youtube", "v3", function() {
        // yt api is ready
    });
}


    $("p").on("click", function(){
        alert("Start Process");

      var request = gapi.client.youtube.search.list({
            part: "snippet",
            type: "video",
            q: "green",
            maxResults: 1,
            order: "viewCount",
            publishedAfter: "2010-01-01T00:00:00Z"
       }); 

        // execute the request
       request.execute(function(response) {
          var results = response.result;
          $("#results").html("");
          //each --> process every all items
          $.each(results.items, function(index, item) {
            //load page 
            $.get("/item/item.html", function(data) {
                //append on the 
                $("#results").append(
                  tplawesome(data, [{"title"   :item.snippet.title, 
											  "videoid" :item.id.videoId}]));
            });
          });
          resetVideoHeight();
       });


    });