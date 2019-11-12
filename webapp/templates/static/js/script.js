$(document).ready(function () {

    function createCanvas(parent, width, height) {
        // get element from the html webpage by its ID and store it in canvas:
        let canvas = document.getElementById("inputCanvas");
        // get object to draw on the canvas:
        canvas.context = canvas.getContext('2d');
        return canvas;
    }// End create canvas function

    // init function to create and draw the canvas on screen to the user:
    function init(container, width, height, fillColor) {
        //Store canvas created in canvas function
        let canvas = createCanvas(container, width, height);
        let ctx = canvas.context;
        ctx.fillCircle = function (x, y, radius, fillColor) {
            this.fillStyle = fillColor;
            this.beginPath();
            this.moveTo(x, y);
            this.arc(x, y, radius, 0, Math.PI * 2, false);
            this.fill();
        };
        ctx.clearTo = function (fillColor) {
            ctx.fillStyle = fillColor;
            ctx.fillRect(0, 0, width, height);
        };
        ctx.clearTo("#fff");

        //Draw function to allow the user draw within the canvas with the moose:
        canvas.onmousemove = function (e) {
            if (!canvas.isDrawing) {
                return;
            }
            let x = e.pageX - this.offsetLeft;
            let y = e.pageY - this.offsetTop;
            let radius = 10;
            let fillColor = 'rgb(102,153,255)';
            ctx.fillCircle(x, y, radius, fillColor);
        };
        canvas.onmousedown = function (e) {
            canvas.isDrawing = true;
        };
        canvas.onmouseup = function (e) {
            canvas.isDrawing = false;
        };
    }

    let container = document.getElementById('canvas');
    //Run init function:
    init(container, 200, 200, '#ddd');

    function clearCanvas() {
        let canvas = document.getElementById("inputCanvas");
        let ctx = canvas.getContext("2d");
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    async function getData() {
        let canvas = document.getElementById("inputCanvas");
        let imageData = canvas.context.getImageData(0, 0, canvas.width, canvas.height);
        let imagedata = imageData.data;

        // Making a post request with image data in the body of the request
        let response = await fetch('/predict', {
            method: 'POST',
            body: imagedata
        });
        // the server responds
        let result = await response.json();
        // Alert user
        alert(result.message)
    }// End getdata function

    $("#clearButton").click(function () {
        clearCanvas();
    });

    $("#sendButton").click(function () {
        getData();
    });
});