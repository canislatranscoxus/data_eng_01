import pymysql.cursors


class CsvLoader:

    conn = None
    num_transactions = 2

    sql_insert = {
        'departments'     : 'INSERT INTO departments(id, department) values(%s,%s);',
        'jobs'            : 'INSERT INTO jobs(id, job) values(%s,%s);',
        'hired_employees' : 'INSERT INTO hired_employees(id,name,datetime,department_id,job_id) values(%s,%s,%s,%s,%s);',
    }

    def connect(self, host, database, user, password ):
        # This method make a connection to mySQL database.
        try:
            conn = None

            print( 'CsvLoader.connect()' )
            print( 'host    : ', host     )
            print( 'database: ', database )
            print( 'user    : ', user     )
            print( 'password: ', password )

            self.conn = pymysql.connect(host        = host,
                                        database    = database,
                                        user        = user,
                                        password    = password,
                                        charset     = 'utf8mb4',
                                        cursorclass = pymysql.cursors.DictCursor)

            return conn
        except Exception as e:
            print('CsvLoader.connect(), error: {}'.format(e))
            raise

    def insert_csv_string(self, table, row_data):
        # This method insert data into table in database.
        # we use the next parameters:
        #   table - The table name in


        try:
            # split the txt string in lines
            error_message = None

            if table not in self.sql_insert:
                error_message = '{} does not exist in the database'.format( table )
                return error_message

            # get the proper insert sql command
            query = self.sql_insert[ table ]

            # split the csv string data in lines
            lines = row_data.split( '\n' )
            print( '\n insert_csv_string(), ... csv row data' )


            cursor = self.conn.cursor()

            i = 0
            for line in lines:
                i = i +1
                line = line.replace( '\r', '' )
                values = line.split( ',' )

                if table == 'hired_employees':
                    # clean date time
                    values[ 2 ] = values[ 2 ].upper().replace( 'Z', '' )

                print( line )
                number_of_rows = cursor.execute(query, values )

                if i % self.num_transactions == 0:
                    # here we execute a batch of inserts.
                    self.conn.commit()

            # If we have a small batch at the end, we insert into database now.
            self.conn.commit()
            print( 'number of lines processed: {}  \n\n'.format( i ) )

            return error_message

        except Exception as e:
            print( 'CsvLoader.insert_csv_string(), error: {}'.format( e ) )

    def __init__(self, num_transactions = 10 ):
        try:
            self.num_transactions = num_transactions
        except Exception as e:
            print( 'CsvLoader.__init__(), error: {}'.format( e ) )
