'''
description : here we expose our REST API. Always include Port in the URL.

method      : GET, POST

urls        :
            https://gatojazz.dev:443
            https://gatojazz.dev:443/csv_load


for debugging locally
            http://127.0.0.1:8000
            http://127.0.0.1:8000/csv_load

'''

from .                          import views
from django.urls                import path
#from django.conf                import settings
#from django.conf.urls.static    import static

app_name = 'csv_load'

urlpatterns = [

    path( 'testdb'  , views.TestDbView.as_view() ),

    path( ''  , views.CsvView.as_view() ),
    path( 'csv_load'  , views.CsvView.as_view() ),

    path( 'backup'  , views.BackupView.as_view() ),
    path( 'restore' , views.RestoreView.as_view() ),
]