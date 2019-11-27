// Function to create a a canvas with width and height and container
function createCanvas(parent, width, height) {
    // get element from the html webpage by its ID and store it in canvas:
    let canvas = document.getElementById("inputCanvas");
    // get object to draw on the canvas:
    canvas.context = canvas.getContext('2d');
    return canvas;
}// End create canvas function

// init function to create and draw the canvas on screen to the user:
function init(width, height, fillColor) {
    //Store canvas created in canvas function
    let container = document.getElementById('canvas');
    let canvas = createCanvas(container, width, height);
    let ctx = canvas.context;
    ctx.fillCircle = function (x, y, radius, fillColor) {
        this.fillStyle = fillColor;
        this.beginPath();
        this.moveTo(x, y);
        this.arc(x, y, radius, 0, Math.PI * 2, false);
        this.fill();
        //Update data element each time the input canvas gets updated:
        document.getElementById("canvas_data").value = document.getElementById("inputCanvas").toDataURL();
    };
    ctx.clearTo = function (fillColor) {
        ctx.fillStyle = fillColor;
        ctx.fillRect(0, 0, width, height);
    };
    ctx.clearTo("#000000");

    //Draw function to allow the user draw within the canvas with the moose:
    canvas.onmousemove = function (e) {
        if (!canvas.isDrawing) {
            return;
        }
        let x = e.pageX - this.offsetLeft;
        let y = e.pageY - this.offsetTop;
        let radius = 10;
        let fillColor = 'rgb(255,255,255)';
        ctx.fillCircle(x, y, radius, fillColor);

    };
    canvas.onmousedown = function (e) {
        canvas.isDrawing = true;
    };
    canvas.onmouseup = function (e) {
        canvas.isDrawing = false;
    };
}

//Run init function:
init(200, 200, '#000000');

function sendCanvasData() {
    let canvas = document.getElementById("inputCanvas");
    let canvas_data_url = canvas.toDataURL();
    console.log(canvas_data_url);

    $.ajax({
        url: '/predict',
        method: 'POST',
        data: {data_url_string: canvas_data_url}
    }).done(function (data) {
        console.log(data)
    });
}//End send function

//Function to clear canvas
function clearCanvas() {
    let canvas = document.getElementById("inputCanvas");
    let ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}//End function


//www.chartjs.org/docs/latest/
//Function to chart prediction
function loadChart(label, data) {

}

function displayChart(data) {

}
