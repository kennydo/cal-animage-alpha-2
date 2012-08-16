google.load("gdata", "1");
google.load("jquery", "1");

var BLOG_FEED_URL = "http://blog.calanimagealpha.com/feeds/posts/default";
var NUM_LATEST_ENTRIES = 6;

function preloadImages(images, path){
	$(images).each(function(){
		$('<img/>')[0].src = path + this;
	});
}
	
function prettyDate(date){
	var days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
	var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];	
	return months[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear();
}

function generateEntryHtml(entry){
	title = entry.getTitle().getText();
	entryHref = entry.getHtmlLink().getHref();
	content = entry.getContent().getText();
	author = entry.getAuthors()[0].getName().getValue();
	date =  entry.getUpdated().getValue().getDate();
	
	commentsText = "View Comments";
	links = entry.getLinks();
	if (links.length >= 2){
		commentsLinkTitle = links[1].getTitle();
		if (commentsLinkTitle.indexOf("Comments") > 0){
			commentsText = commentsLinkTitle;
		}
	}
	
	return '<article>\
		<header>\
			<span class="time">' + prettyDate(date) + '</span>\
			<h1>' + title + '</h1>\
		</header>\
		<section><p>' + content + '</p></section>\
		<footer>\
			<span class="author">Posted by ' + author + '</span> - \
			<span class="comments-link"><a href="' + entryHref + '">' + commentsText + '</a></span> \
		</footer>\
		</article>';
}
var entries;
function updateBlogView(feedRoot){
	entries = feedRoot.feed.getEntries();
	if (entries.length > 0){
		entry_htmls = [];
		for (i = 0; i < NUM_LATEST_ENTRIES && i < entries.length; i++){
			entry_htmls.push(generateEntryHtml(entries[i]));
			$("#latest-blog-entries").html(entry_htmls.join("<hr />"));
		}
	} else {
		handleUpdateBlogViewError("");
	}
}

function handleUpdateBlogViewError(error){
	errorHtml = 'There was an error loading the latest entry from <a href="http://blog.calanimagealpha.com">our blog</a>.';
	$("#latest-blog-entries").html(errorHtml);
}

google.setOnLoadCallback(function(){
	
	if ($("#latest-blog-entries").length > 0){
		// This id is only on the main page
		var bloggerService = new google.gdata.blogger.BloggerService('GetLatestEntry');
		bloggerService.getBlogFeed(BLOG_FEED_URL + '?max-results=' + NUM_LATEST_ENTRIES, updateBlogView, handleUpdateBlogViewError);
	}
	
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
