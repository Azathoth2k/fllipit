# FLLiPit
A simple pit display for use at Maine FIRST Lego League Events

###Libraries/ Dependencies:
* Python 2.7
* Flask
* Flask-SQLAlchemy
* Flask-RESTful
* PyPyODBC
* JQuery
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

$ cd fllipit
$ virtualenv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

Create the database (only if using test database instead of an actual MS Access database)
```
#!text

(venv)$ python create_db.py
```

Run the application

```
#!text

$ python fllipit.py
```

### Running on Windows with MS Access Database:
```
#!text

$ git clone https://rtfoley@bitbucket.org/rtfoley/fllipit.git
```

Create a virtual environment and install dependencies

```
#!text

> cd fllipit
> virtualenv venv
> .\\venv\Scripts\activate
(venv) > pip install -r requirements.txt
```

Modify the following properties in config.py:
```
#!python
DEBUG = False
EVENT_NAME = 'Maine FLL Championship'
TEST_DB = False
DB_FILE = "C:\\path\\to\\Access Database\\database.accdb"
```

Run the application

```
#!text

(venv) > python fllipit.py
```