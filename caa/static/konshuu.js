PDFJS.workerSrc = 'http://calanimagealpha.com/pdfjs/build/pdf.worker.js';
var konshuu_canvas = document.getElementById("konshuu_reader");
konshuu_canvas.textBaseline = "top";
var konshuu_progress = document.getElementById("konshuu_progress");

var rendering = null;

function renderPage(pdf, pageNumber)
{
    function render(pdf, pageNumber)
    {
        rendering = pdf.getPage(pageNumber).then(function(page) {
                var viewport = page.getViewport(1.0);

                var aspect = viewport.height / viewport.width;

                konshuu_canvas.width = konshuu_canvas.clientWidth * window.devicePixelRatio;
                konshuu_canvas.height = konshuu_canvas.width * aspect;

                rendering = page.render({
                    canvasContext: konshuu_canvas.getContext('2d'),
                    viewport: page.getViewport(konshuu_canvas.width / viewport.width)
                }).then (function() {
                    rendering = null;
                    konshuu_canvas.getContext('2d').font = '1em Verdana';
                    konshuu_canvas.getContext('2d').fillText("Page "+pageNumber+" of "+pdf.numPages, 30, 30);
                });
            });
    }

    if(!rendering)
    {
        render(pdf, pageNumber);
    }
}

var listener = null;

document.getElementById("konshuu_selection").onchange = function()
{
    var pageNumber = 1;
    var file = document.getElementById("konshuu_selection").value;

    if(file == "default")
        return;

    PDFJS.getDocument('http://calanimagealpha.com/konshuu/' + file).then(function(pdf) {
        renderPage(pdf, 1);
        konshuu_canvas.style.display = "block";
        konshuu_progress.style.display = "none";

        function keyupListener(e)
        {
            if(rendering)
                return;

            if(e.keyCode == 37 && pageNumber != 1)
            {
                pageNumber--;
                renderPage(pdf, pageNumber);
            }
            if(e.keyCode == 39 && pageNumber != pdf.numPages)
            {
                pageNumber++;
                renderPage(pdf, pageNumber);
            }
        }
        listener = keyupListener;
        document.addEventListener("keyup", listener);
    });

        if(listener)
        {
                document.removeEventListener("keyup", listener);
        }

    konshuu_progress.style.display = "block";
};