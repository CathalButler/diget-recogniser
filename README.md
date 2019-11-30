## Emerging-Technologies-Project
### Cathal Butler | G00346889 | Final Year Software Development
A jupyter notebook containing code and documentation to train a model on the MNIST dataset as well as a flask web 
application that allows user draw a digit from 0 -> 9 and submit it. The application will process the image and make 
prediction from the trained model and return answer.


### [Try it live here](http://34.240.7.87/)

![example](https://github.com/butlawr/Emerging-Technologies-Project/blob/master/assets/example.gif)

### Environment Setup
The environment setup needed:
 
 * Install [Git](https://git-scm.com/downloads) to clone the project via repo URL or download the .zip from the website:
    * `git clone https://github.com/butlawr/Emerging-Technologies-Project`
 * Install [Python 3.7 ](https://www.python.org/downloads/)
 * Set up a [python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) inside the project directory:
    * `cd /Emerging-Technologies-Project`
    * `python3 -m venve ./venv`
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

### Development & Testing
This project was developed on my own personal laptop running
* OS: [Manjaro Linux](https://manjaro.org/download/official/kde/)
* Kernel: 5.3.12
* Python 3.7.4
* [PyCharm 2019.2.5 (Professional Edition)](https://www.jetbrains.com/pycharm/)
  - Build #PY-192.7142.56, built on November 19, 2019

Testing was carried out on my personal machine listed above as well a [AWS Ubuntu Server](https://aws.amazon.com/) this
machine also host the application using [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) & [Nginx](https://www.nginx.com/)
* OS: [Ubuntu 18.04.3 LTS](https://ubuntu.com/download/desktop)
* Kernel: 4.15.0-1054-aws
* Python 3.6.9

Windows 10 to be tested!
