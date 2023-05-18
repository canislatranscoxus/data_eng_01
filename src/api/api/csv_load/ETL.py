import os
from datetime               import datetime

from .Extractor import Extractor
from .Transformer           import Transformer
from .Loader                import Loader

from .avro.AJobs            import AJobs
from .avro.ADepartments     import ADepartments
from .avro.AHiredEmployees  import AHiredEmployees

class ETL:
    params   = None
    table    = None
    csv_data = None
    loader   = None

    def backup(self):
        # this method create a backup from mySQL to avro files.
        try:
            print( 'ETL.backup ... begin' )
            departments = ADepartments( self.params )
            jobs = AJobs( self.params )
            hired_employees = AHiredEmployees( self.params )

            # create folder for new backups
            dt = datetime.now()
            tar_dir = dt.strftime('%Y%m%d_%H%M%S')
            tar_dir = os.path.join( self.params[ 'BACKUP_PATH' ], tar_dir)
            os.mkdir(tar_dir)

            # make backup
            departments.export(tar_dir)
            jobs.export(tar_dir)
            hired_employees.export(tar_dir)

            print('ETL.backup ... end')

        except Exception as e:
            print( 'ETL.backup(), error: {}'.format( e ) )
            raise

    def restore(self, src_dir ):
        try:
            departments = ADepartments( self.params )
            jobs = AJobs( self.params )
            hired_employees = AHiredEmployees( self.params )

            # make backup
            departments.restore(src_dir)
            jobs.restore(src_dir)
            hired_employees.restore(src_dir)
        except Exception as e:
            print( 'ETL.restore(), error: {}'.format( e ) )
            raise


    def run(self ):
        # This method insert data into table in database.
        # we use the next parameters:
        #   table - The table name in
        try:
            extractor   = Extractor()
            transformer = Transformer( self.table )
            lines       = extractor.get_lines( self.csv_data )

            i = 0
            for line in lines:
                try:
                    i = i +1
                    values = transformer.get_clean_values( line )
                    self.loader.insert( values )

                    if i % self.num_transactions == 0:
                        # here we execute a batch of insert transactions.
                        self.loader.commit()
                except Exception as e:
                    print('ETL.run() for line, error: {}'.format(e))
                    raise

            # If we have a small batch at the end, we insert into database now.
            self.loader.commit()
            print( 'number of lines processed: {}  \n\n'.format( i ) )

            return i

        except Exception as e:
            print( 'ETL.run(), error: {}'.format( e ) )
            raise

    def __init__(self, params

                 #host, database, user, password, table, csv_data,
                 #num_transactions = 10

                 ):
        try:
            self.params   = params
            self.table    = params[ 'table'    ]
            self.csv_data = params[ 'csv_data' ]
            self.num_transactions = int(params['NUM_TRANSACTIONS'])
            self.loader = Loader( params )

        except Exception as e:
            print( 'ETL.__init__(), error: {}'.format( e ) )


