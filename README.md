# FLLiPit
A simple pit display for use at Maine FIRST Lego League Events

###Libraries/ Dependencies:
* Python 2.7
* Flask
* Flask-RESTful
* Flask-conditional
* JQuery
* Moment.js
* Bootstrap

### Getting started
Clone the repository

```
#!text

$ git clone https://rtfoley@bitbucket.org/rtfoley/fllipit.git
```

Create a virtual environment and install dependencies

```
#!text

$ cd kmon
$ virtualenv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

Create the database
```
#!text

$ cd kmon
$ virtualenv venv
$ source venv/bin/activate
(venv)$ python
>>> from fllipit import DB, Team
>>> DB.create_all()
>>> quit()
```

Run the application

```
#!text

$ python fllipit.py
```