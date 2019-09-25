# CSCI 4380 - Database Systems - Project

This project stores, retrieves and renders information regarding motor vechicle accidents in 2015.

## Loading the application's data

### Installing required modules 

```
pip3 install -r requirements.txt
```

### Populating the database

To populate the database run:
```
psql postgres postgres < setup.sql
python3 load_data.py
```
The postgres account motordb has the password motordb

## Viewing the application

The application contains a lightweight web server and a psql backend.
To view it run:
```
python3 application.py
```
The web server runs on localhost:5000
