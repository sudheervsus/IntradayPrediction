from django.urls import path
from django.conf.urls import url
from .views import StockPredict

urlpatterns = [
        url(r'^stockpredict/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', StockPredict.as_view(), name='stock_predict'),
        #path('', HomePageView.as_view(), name='Home')
        ]
