import pymysql.cursors

from django.shortcuts               import render
from django.conf                    import settings

from rest_framework                 import status
from rest_framework.authentication  import BasicAuthentication
from rest_framework.permissions     import AllowAny
from rest_framework.response        import Response
from rest_framework.views           import APIView

from .ETL                           import ETL

# Create your views here.

class TestDbView( APIView ):
    def get(self, request):
        try:
            conn = pymysql.connect(host     = settings.MYSQL_HOST,
                                   database = settings.MYSQL_NAME,
                                   user     = settings.MYSQL_USER,
                                   password = settings.MYSQL_PASSWORD,
                                   port     = 3306,
                                   charset  = 'utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            cursor.execute( 'select * from departments;' )
            result = cursor.fetchall()
            #conn.commit()

            for i in result:
                print( i )

            return Response( "database test ..OK. \n table deparments \n {}".format( result) )
        except Exception as e:
            print( 'TestDb.get(), error: {}'.format( e ) )

class CsvView( APIView ):

    authentication_classes  = ( BasicAuthentication, )
    permission_classes      = ( AllowAny,)

    def get( self, request ):
        print( 'api.csv_load.views.CsvLoader.get() ... begin' )
        print('... working ok')
        print('api.csv_load.views.CsvLoader.get() ... begin')
        return Response( "test 1 - api is running OK" )


    def post(self, request, *args, **kwargs):
        try:
            params = settings.__dict__['_wrapped'].__dict__
            params[ 'table'    ] = request.data[ 'table'    ]
            params[ 'csv_data' ] = request.data[ 'csv_data' ]
            etl = ETL( params )
            etl.run()
            return Response( 'ETL finished successfully' )
        except Exception as e:
            print('csv_load.views.post(), error: {}'.format(e))
            return Response( 'Error loading csv data' )

