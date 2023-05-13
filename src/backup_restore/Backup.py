import pymysql.cursors
import os
from Params import Params


class Backup:

    conn = None

    def connect(self, host, database, user, password ):
        # This method make a connection to mySQL database.
        try:
            print( 'Backup.connect()' )
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

        except Exception as e:
            print('Backup.connect(), error: {}'.format(e))
            raise


