from abc import ABC
import json
import os
import pymysql.cursors

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


class ITable( ABC ):
    params = None
    table_name = ''
    conn   = None
    schema = {}

    sql_restore = {
        'departments'     : "INSERT INTO departments(id, department) values({id},'{department}');",
        'jobs'            : "INSERT INTO jobs(id, job) values({id},'{job}');",
        'hired_employees' : "INSERT INTO hired_employees(id,name,datetime,department_id,job_id) values({id},'{name}','{datetime}',{department_id},{job_id});",
    }


    def connect(self, host, database, user, password ):
        # This method make a connection to mySQL database.
        try:
            print( 'ITable.connect()' )
            print( 'host    : ', host     )
            print( 'database: ', database )
            print( 'user    : ', user     )
            print( 'password: ', password )

            self.conn = pymysql.connect(host        = host,
                                        database    = database,
                                        user        = user,
                                        password    = password,
                                        port        = 3306,
                                        charset     = 'utf8mb4',
                                        cursorclass = pymysql.cursors.DictCursor)
            print( 'ITable.connect() ... ok' )
        except Exception as e:
            print('ITable.connect(), error: {}'.format(e))
            raise

    def clean_export_row(self, d):
        pass

    def export(self, tar_dir ):
        # export table as avro file in the target directory
        try:
            file_name   = os.path.join( tar_dir, self.table_name ) + '.avro'
            sql_command = 'select * from {}'.format( self.table_name )
            cursor      = self.conn.cursor()
            cursor.execute(sql_command)
            result = cursor.fetchall()
            # conn.commit()

            schema = avro.schema.parse( json.dumps( self.schema ) )
            d = {}
            writer = DataFileWriter(open( file_name, "wb"), DatumWriter(), schema)
            for d in result:
                self.clean_export_row(d)
                writer.append( d )
            writer.close()
        except Exception as e:
            print( 'ITable.export(), table: {}, error: '.format( self.table_name, e ) )
            raise


    def restore(self, src_dir ):
        # load data from avro file to table in database.
        try:
            file_name        = os.path.join( src_dir, self.table_name ) + '.avro'
            cursor           = self.conn.cursor()
            num_transactions = int( self.params['NUM_TRANSACTIONS'] )
            reader           = DataFileReader(open( file_name, "rb"), DatumReader())
            i = 0
            for row in reader:
                i = i + 1
                sql_command = self.sql_restore[self.table_name].format( **row )
                cursor.execute(sql_command)
                if i % num_transactions == 0:
                    self.conn.commit()

            self.conn.commit()
            reader.close()
        except Exception as e:
            print( 'ITable.restore(), table: {}, error: '.format(self.table_name, e) )
            raise

    def __init__(self, params ):
        try:
            self.params = params

            self.connect(params['MYSQL_HOST'], params['MYSQL_NAME'],
                params['MYSQL_USER'], params['MYSQL_PASSWORD'] )

        except Exception as e:
            print( 'ITable.__init__(), error: '.format( e ) )
            raise


