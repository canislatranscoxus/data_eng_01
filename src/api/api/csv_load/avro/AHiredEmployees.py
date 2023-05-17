from .ITable import ITable

from datetime import timezone

class AHiredEmployees( ITable ):
    table_name = 'hired_employees'
    schema ={
        'namespace' : 'company01.avro',
        'type'      : 'record',
        'name'      : 'departments',
        'fields'    : [
            {'name': 'id'           , 'type': ['int'   , 'null' ]},
            {'name': 'name'         , 'type': ['string', 'null' ] },

            {'name': 'datetime'     ,
             'type': {'type': 'long', 'logicalType': 'timestamp-millis' },
            },

            {'name': 'department_id', 'type': ['int', 'null']},
            {'name': 'job_id'       , 'type': ['int', 'null']},
         ]
    }

    def clean_export_row(self, d):
        # here we clean or prepare any data before export to avro file
        try:
            #ts = d['datetime'].replace(tzinfo= timezone.utc).timestamp()
            #ts = 1627401728
            ts = d['datetime'].replace(tzinfo=timezone.utc)
            d['datetime'] =  ts
        except Exception as e:
            print( 'AHiredEmployees.clean_export_row(), error: '.format( self.table_name, e ) )
            raise





