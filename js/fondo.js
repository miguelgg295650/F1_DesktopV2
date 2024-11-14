class Fondo {
    getImages() {
        console.log("Image URL:"); 
        const flickrAPI = "https://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
        $.getJSON(flickrAPI, {
            tags: "landscape",
            tagmode: "any",
            format: "json",
        }).done(function(data) {
            if (data.items.length > 0) {
                const r = Math.floor(Math.random() * data.items.length);

                const imageUrl = data.items[r].media.m;

                if (imageUrl) {
                    
                    $('body').css('background-image', 'url(' + imageUrl + ')');
                    $('body').css('background-size', 'cover');
                    $('body').css('background-position', 'center');
                    $('body').css('background-attachment', 'fixed');
                    $('body').css('background-repeat', 'no-repeat');
                    $('body').css('height', '100vh');
                } else {
                    console.log("No valid image URL found.");
                }
            
            } else {
                document.write("<h1>No fotos</h1>");
            }
        });
    }
}


const f = new Fondo();
f.getImages();



    