## Emerging-Technologies-Project
### Cathal Butler | G00346889 | Final Year Software Development
A jupyter notebook containing code and documentation to train a model on the MNIST dataset as well as a flask web 
application that allows user draw a digit from 0 -> 9 and submit it. The application will process the image and make 
prediction from the trained model and return answer.

### Environment Setup
The environment setup needed:
 
 * Install [Git](https://git-scm.com/downloads) to clone the project via repo URL or download the .zip from the website:
    * `git clone https://github.com/butlawr/Emerging-Technologies-Project`
 * Install [Python 3.7 ](https://www.python.org/downloads/)
 * Set up a [python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) inside the project directory:
    * `cd /Emerging-Technologies-Project`
    * `pip install virtualenv`
    * `virtualenv venv` 
        * this will create a virtual environment called venv, you may name it what you like.
 * To activate virtual environment created inside the project directory:
    * `source venv/bin/activate`
    
 * Install the [required python packages](https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip) listed in the [requirements.txt](https://github.com/butlawr/Emerging-Technologies-Project/blob/master/requirements.txt) file, this can be done by:
    * `pip install -r requirements.txt`
    * Note: Still in development, more requirements may be added.
   
### How to run Jupyter Notebook
Before you begin to run this application please make sure you refer to the environment setup explained below. 

* `cd /Emerging-Technologies-Project`
* Activate environment: `source venv/bin/activate`
* To run the notebook: `jupyter notebook`
    - Notebook accessible @ `http://localhost:8888`

### How to to run Number Prediction Flask Webapp

* `cd /Emerging-Technologies-Projec/`
* Activate environment if you have not already: `source venv/bin/activate`
* `cd /webapp`
* `export FLASK_APP=app.py && flask run`
    - Webapp accessible @ `http://127.0.0.1:5000/`
