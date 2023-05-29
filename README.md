# PoC of ETL ingesting csv data from REST API to mySQL on Google Cloud GCP.


#### Arturo Alatriste Trujillo

arturo_alatriste@hotmail.com

https://github.com/canislatranscoxus/data_eng_01

https://aatvelo4.wn.r.appspot.com
https://company.gatojazz.dev/


## Abstract

This is a PoC of a Rest API created in Python Django. 
The solution is a ETL, Extract Tansform Load.
We expose an url point to send raw data in csv format, 
next in the backend python code take the row data and Transform it,
and Loaded into mySQL database.
Also, we have one API for basckup tables to avro files
and another API to restore database tables from avro files.

## usage of CSV ETL

Test the REST API connectivity.
If we are running django locally, we can open a web browser and use this url

```
https://127.0.0.1:8000/csv_load
```

there we can use a GET method, just to test connectivity, and verify the api is up and running.

Also, we can test the POST method,
with this we can insert new data to the database.

If we deploy to a cloud environment such as Google GCP,
we can use Google App Engine to run our Django Solution, and use a url like this

```
https://aatvelo4.wn.r.appspot.com/csv_load
```



Note: Remember to include the port number. 
      This can be different, depending on the environment, platform or cloud provider. 

### ingesting csv data to departments table

open the url api endpoint, for example the local

```
http://127.0.0.1:8000/csv_load
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


```
{
    "table": "jobs",
    "csv_data": "1,Marketing Assistant\n2,VP Sales\n3,Biostatician IV\n4,Account Representant\n5,VP Marketing\n6,Environmental Spec\n7,Software Consultant\n8,Office Assistant III\n9,Information Systems\n10,Desktop Suport Tech"
}
```

### how to make database backup

This feature create three avro files one per each table in our mySQL database.
We set the backup folder parameter in the environment variable

```
BACKUP_PATH
```

use a tool like postman to hit the rest API url with the next parameters

|---|---|
| method | post |
| url in local environment | http://127.0.0.1:8000/backup |


### How to make a database restore

use a tool like postman to hit the rest API url with the next parameters
and in the body, pass the source directory that contain the avro files.

|---|---|
| method | post |
| url in local environment | http://127.0.0.1:8000/restore |
| body  | { "src_dir" : "<folder_path_with_avro_files>"  }  |
