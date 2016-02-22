# Item Catalog Web Application
A database driven web application that allows a categorized catolog of items to be managed.<br/>
Anonymous users can browse the web site, whilst users that are authenticated with Facebook or Google 
can add content to the site.


## Prerequisites

The module requires **Python 2.7** and **SQLite** to to be already installed.<br/>
The module also depeneds on the **SQLAlchemy** Python module to access the database.
Flask microframework for Python.
Flask extensions:
Flask-SQLAlchemy
 -  pip install Flask-SQlAlchemy


## Installation
Clone this repository on the command line, to get the files.
```Shell
git clone https://github.com/iainbx/tournament-results.git
```

### Files
The repository contains the following files.
####run.py
Start the web server

###Database Setup
To create the catalog database in SQLite, with it's tables and views,
run the following `python` command on the command line.
```Shell
python database_setup.py
```
## Usage

###Browsing the web site
Once the database has been successfully created,
you can run the web site with the following `python` command on the 
command line.
```Shell
python run.py
```

###API

