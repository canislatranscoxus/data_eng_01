from django.shortcuts import render
from django.conf                import settings

from rest_framework                 import status
from rest_framework.authentication  import BasicAuthentication
from rest_framework.permissions     import AllowAny
from rest_framework.response        import Response
from rest_framework.views           import APIView

#from django.shortcuts           import get_object_or_404
#from .serializers               import WebhookSerializer
#import json

from .CsvLoader         import CsvLoader

# Create your views here.


class CsvView( APIView ):

    authentication_classes  = ( BasicAuthentication, )
    permission_classes      = ( AllowAny,)




    def get( self, request ):
        print( 'api.csv_load.views.CsvLoader.get() ... begin' )
        return Response( "test 1 - api is running OK" )


    def post(self, request, *args, **kwargs):
        print( 'api.csv_load.views.CsvLoader.post() ... begin' )
        params = request.data

        # debug code to monitor we are getting the parameters.
        #s = json.dumps( params, indent = 4 )
        #print( s )

        table_name = params[ 'table' ]
        #self.insert_csv_string( params )
        csvLoader = CsvLoader( num_transactions= settings.NUM_TRANSACTIONS )

        csvLoader.connect(
             settings.MYSQL_HOST
            ,settings.MYSQL_NAME
            ,settings.MYSQL_USER
            ,settings.MYSQL_PASSWORD )

        csvLoader.insert_csv_string(params[ 'table' ], params[ 'csv_data' ] )

        print( 'api.csv_load.views.CsvLoad.post() ... end' )
        return Response( 'data loaded into {} table'.format( table_name ) )

