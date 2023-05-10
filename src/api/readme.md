# Readme

This is a PoC of a Rest API created in Python Django.
We expose an url point to send raw data in csv format,
next the python backend code insert that data in a 
mySQL database.

## usage

Test the REST API connectivity.
If we are running django locally, we can open a web browser and use this url

```
http://127.0.0.1:8000/csv_load/loader
```

there we can use a GET method, just to test connectivity, and verify the api is up and running.

Also, we can test the POST method,
with this we can insert new data to the database.

If we deploy to a cloud environment such as Google GCP,
we can use Google App Engine, and use a url like this

```
https://gatojazz.dev:443/csv_load/loader
```

Important Note: Remember to always include the port number. 
                This can be different, depending on the environment, platform or cloud provider. 

### ingesting csv data to departments table

open the url api endpoint, for example the local

```
http://127.0.0.1:8000/csv_load/loader
```

and in the body pass a json with the parameters

table - This is the name of the target table in the sql database.

csv_data - This is the raw data in csv format in a string. The lines must be separated by 
           new line character. And the values must separated by comma. 

#### Body example:

In the next example we specify the table "departments", and we specify two departments in the 
csv_data parameter. See the parameters below:


```
{
    "table": "departments",
    "csv_data": "1,Product Management\n\r2,Sales"
}
```