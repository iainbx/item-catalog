# Item Catalog Web Application
A Python web application for managing a categorized catolog of items.<br/>


## Features
* Third party authentication and authorization with Google or Facebook, using OAuth.
* Anonymous users are allowed to view the web site.
* Authenticated users can create categories and items.
* Authenticated users can edit and delete their own content.
* Item images can be uploaded and displayed in the site.
* JSON endpoint for retrieving all items in the catalog.
* Atom feed endpoint for subscribing to latest items.
* Cross-Site Request Forgery protection for POST requests. 


## Prerequisites
The application is written in **Python 2.7** and uses a [SQLite](https://www.sqlite.org/) database.<br/>
Database access is handled by the [SQLAlchemy](http://www.sqlalchemy.org/) ORM.<br/>
The web application is built with the [Flask](http://flask.pocoo.org/) framework and utilizes the 
[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) and [Flask-WTF](https://flask-wtf.readthedocs.org) Flask extensions.<br/>
Application dependencies are listed in the **requirements.txt** file.

## Installation
To get the files, clone this repository on the command line.
```Shell
git clone https://github.com/iainbx/item-catalog.git
```

### Files And Folders
The repository contains the following notable files and folders.
####config.py
Application wide configuration settings.
####catalog.db
Application SQLite database.
####create_sample_data.py
Script to populate the database with sample data.
####database_setup.py
Script to create the SQLite database and schema.
####requirements.txt
Application dependencies.
####run.py
Script to start the web server and load the application.
####catalog/forms.py
Flask-WTF forms for the application.
####catalog/models.py
SQLAlchemy database model for the application.
####catalog/views.py
Flask view functions for the application.
####catalog/templates
Folder containing HTML templates for the views in the application.

###Database Setup
The project includes a SQLite database called **catalog.db** that is already populated with
sample data, so no database setup is necessary, unless you want to.<br/><br/>
To create the catalog database, with it's tables and views,
run the following `python` command on the command line.
```Shell
python database_setup.py
```
To populate the database with sample data, run the following command.
```Shell
python create_sample_data.py
```

## Usage

###Browsing the web site
Once the database has been successfully created,
you can start the web server with the following `python` command on the 
command line.
```Shell
python run.py
```
Then, you can browse to the web site at **http://localhost:8000**.

###Adding Content
You will need to login with your Facebook or Google credentials
 in order to add categories or items to the catalog.
 You can only edit or delete content that you have added.

###API
The application provides a JSON endpoint at **http://localhost:8000/catalog/json** 
to retrieve all the items in the catalog.<br/>
There is also an Atom feed endpoint at **http://localhost/catalog/recent.atom** to subscribe 
to a feed of the latest items.

