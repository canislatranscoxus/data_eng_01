'''
description : here we expose our REST API. Always include Port in the URL.

method      : GET, POST

urls        :
              https://www.oasisverde.dev:443/en/webhook/paid_order_noti
              https://oasisverde.dev:443/en/csv_load/csvloader

for debugging locally
            http://127.0.0.1:8000/en/csv_load/csvloader
'''

from .                          import views
from django.urls                import path
#from django.conf                import settings
#from django.conf.urls.static    import static



urlpatterns = [
    path( 'loader'  , views.CsvView.as_view() ),
]