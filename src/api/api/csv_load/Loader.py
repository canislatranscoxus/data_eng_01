import pymysql.cursors

class Loader:
    table  = None
    conn   = None
    cursor = None


    sql_insert = {
        'departments'     : "INSERT INTO departments(id, department) values({},'{}');",
        'jobs'            : "INSERT INTO jobs(id, job) values({},'{}');",
        'hired_employees' : "INSERT INTO hired_employees(id,name,datetime,department_id,job_id) values({},'{}','{}',{},{});",
    }


    def connect(self, host, database, user, password ):
        # This method make a connection to mySQL database.
        try:
            print( 'Loader.connect()' )
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
            print( 'Loader.connect() ... ok' )
        except Exception as e:
            print('Loader.connect(), error: {}'.format(e))
            raise


    def insert(self, values):
        try:
            sql_command    = self.sql_insert[ self.table ].format(*values)
            number_of_rows = self.cursor.execute(sql_command)
            return number_of_rows
        except Exception as e:
            print( 'Loader.insert(), error: {}'.format(e) )

    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            print( 'Loader.insert(), error: {}'.format(e) )


    def __init__(self, params ):
        try:
            self.table  = params[ 'table' ]

            self.connect(
                params['MYSQL_HOST'], params['MYSQL_NAME'],
                params['MYSQL_USER'], params['MYSQL_PASSWORD'] )

            self.cursor = self.conn.cursor()
        except Exception as e:
            print( 'Loader.__init__(), error: {}'.format(e) )
