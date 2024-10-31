class Fondo{
    getImages(){
        var flickrAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
        $.getJSON(flickrAPI, 
            {
                tags: "F1",
                tagmode: "any",
                format: "json"
            })
        .done(function(data) {
            $.each(data.items, function() {
                if (data.items.length > 0) { 
                    document.getElementsByClassName("FotoInicio")[0].src = data.items[0].media.m; 
                }else{
                    document.write("<h1>No fotos</h1>");
                }
                
            })})
    }
   
 
}
var f = new Fondo();
f.getImages();
   
