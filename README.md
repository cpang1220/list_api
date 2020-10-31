# List API

This API has the following functions:

- **Returns the input list**

- **Returns the sum of input list**

## Requirements
The application requires:
1. Python version 3.7
2. Flask version 1.1.2


## Usage
API path which returns the input list (HTTP GET method)
```
/input_list
```
API path which returns the sum of input list (HTTP GET method)
```
/total
```

## Functions
The input list of numbers data is hard-coded and retrieved from the localhost api.

The script can be found in the path: app/list_sum.py
[list_sum](https://github.com/cpang1220/list_api/blob/master/app/list_sum.py)

The following functions are applied to calculate the sum of numbers list in this API application.
1. Retrieve the input list of numbers from the input_list api configured in localhost.
2. Output the sum of list result by using the sum(list) function.


## API Documentation
The API reference can be found in the swagger.yml file [swagger.yml](https://github.com/cpang1220/list_api/blob/master/swagger.yml)

## Run application
Run application with commands using Flask
```
set FLASK_APP=run.py
flask run
```

## Test
In terminal, run the following command to execute unit test cases without coverage.
```
python manage.py test
```

In terminal, run the following command to execute test with coverage.
```
nosetests --with-coverage --cover-package=app
```

## Automation tools
1. The application includes a Procfile file for users to upload the API application to Heroku. [Procfile](https://github.com/cpang1220/list_api/blob/master/Procfile)
