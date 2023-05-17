from .ITable import ITable

class ADepartments( ITable ):

    table_name = 'departments'

    schema ={
        'namespace' : 'company01.avro',
        'type'      : 'record',
        'name'      : 'departments',
        'fields'    : [
             {'name': 'id'        , 'type': ['int'   , 'null'] },
             {'name': 'department', 'type': ['string', 'null'] },
         ]
}