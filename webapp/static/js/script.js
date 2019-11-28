// Function to create a a canvas with width and height and container
function createCanvas(parent, width, height) {
    // get element from the html webpage by its ID and store it in canvas:
    let canvas = document.getElementById("input_canvas");
    // get object to draw on the canvas:
    canvas.context = canvas.getContext('2d');
    return canvas;
}// End create canvas function

// Init function to create and draw the canvas on screen to the user:
function init(width, height, fillColor) {
    //Get canvas element from the html page with tag canvas
    let container = document.getElementById('canvas');
    //Create a new canvas from the function above with the container element being the 'canvas' element from the html
    // Sets it width and height to the init() functions width and height
    let canvas = createCanvas(container, width, height);
    let ctx = canvas.context;
    ctx.fillCircle = function (x, y, radius, fillColor) {
        this.fillStyle = fillColor;
        this.beginPath();
        this.moveTo(x, y);
        this.arc(x, y, radius, 0, Math.PI * 2, false);
        this.fill();
        //Update data element each time the input canvas gets updated:
        document.getElementById("canvas_data").value = document.getElementById("input_canvas").toDataURL();
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
    canvas.onmousedown = function () {
        canvas.isDrawing = true;
    };
    canvas.onmouseup = function () {
        canvas.isDrawing = false;
    };
}//End init() function

// Run init function
init(200, 200, '#000000');

// Functions which gets the user input canvas data, converts it to a data URL which is then POSTED to backend /predict
// which will process the data URL through the trained model and return a predicted number.
function sendCanvasData() {
    //Get input canvas data
    let canvas = document.getElementById("input_canvas");
    // Convert it to a data URL
    let canvas_data_url = canvas.toDataURL();

    //Make a POST request with the data URL
    $.ajax({
        url: '/predict',
        method: 'POST',
        data: {data_url_string: canvas_data_url}
    }).done(function (data) {
        // Log backend response and output the number to the frontend HTML page
        console.log('Neural Network predicted a:' + data['predicted_number']);
        $("#result").empty().append(data['predicted_number']);
        displayChart(data['prediction'][0])
    });
}//End send function

//Function to clear canvas
function clearCanvas() {
    let canvas = document.getElementById("input_canvas");
    let ctx = canvas.getContext("2d");
    //Fill over the old canvas
    ctx.rect(0, 0, canvas.width, canvas.height);
    //Set background colour to
    ctx.fillStyle = "#000000";
    ctx.fill();
}//End function


//www.chartjs.org/docs/latest/
//Function to chart prediction
let chart = "";
let firstTime = 0;

function loadChart(label, data) {
    let ctx = document.getElementById('chart_box').getContext('2d');
    //Creating a new Chart of type 'bar ' that will display label numbers 0->9 on the x-axis.
    chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data: {
            labels: label,
            datasets: [{
                //Heading
                label: " prediction",
                backgroundColor: '#f50057',
                borderColor: 'rgb(255, 99, 132)',
                //Array data received back from the POST request made to the API
                data: data,
            }]
        },
        // Configuration options
        options: {
            responsive: false
        }
    });
}//End function

function displayChart(data) {
    //Labels for the x-axis 0->9, as many that are in the MNIST dataset
    let label = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    if (firstTime === 0) {
        //Load new chart with labels and response data from the POST request
        loadChart(label, data);
        firstTime = 1;
    } else {
        //Remove chart
        chart.destroy();
        loadChart(label, data);
    }
    document.getElementById('chart_box').style.display = "block";
}//End displayChart
