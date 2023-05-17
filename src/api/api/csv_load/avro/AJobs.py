from .ITable import ITable

class AJobs( ITable ):

    table_name = 'jobs'

    schema ={
        'namespace' : 'company01.avro',
        'type'      : 'record',
        'name'      : 'departments',
        'fields'    : [
             {'name': 'id' , 'type': ['int', 'null'     ] },
             {'name': 'job', 'type': ['string', 'null'  ] },
         ]
}