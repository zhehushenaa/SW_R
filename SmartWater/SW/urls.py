from django.conf.urls import url
from SW import views


urlpatterns=[

    url(r'/index',views.index),
    url(r'/back',views.back),
    url(r'/sensorscan',views.sensorscan),
    url(r'/scandata1',views.scandata1),
    url(r'/sensorrecord',views.sensorrecord),

]