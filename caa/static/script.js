google.load("gdata", "1");
google.load("jquery", "1");

function preloadImages(images, path){
	$(images).each(function(){
		$('<img/>')[0].src = path + this;
	});
}
	
google.setOnLoadCallback(function(){
	
	if (previewImages.length > 0){
		//Preload the images
		preloadImages(previewImages, previewsFolder);
	
		var previewImg = $('<img/>').appendTo('#next-showing .preview').attr('alt', 'Showing Preview Image');
		var imgIndex = Math.round(Math.random() * (previewImages.length - 1));
		previewImg.attr('src', previewsFolder + previewImages[imgIndex]);

		var changeImgDelay = 7000;
		function changeImg(){
			imgIndex = imgIndex + 1;
			if (imgIndex > (previewImages.length - 1)){
				imgIndex = 0;
			}
			
			$('#next-showing .preview').css('background-image', 'url(' + previewsFolder + previewImages[imgIndex] + ')');
			previewImg.fadeOut('slow', function(){
				previewImg.attr('src', previewsFolder + previewImages[imgIndex]).show();
				window.setTimeout(changeImg, changeImgDelay);
			});
		}
		if (previewImages.length > 1){
			window.setTimeout(changeImg, changeImgDelay);
		}
	}
});
