from django.conf.urls import url
from SW import views


urlpatterns=[

    url(r'/index',views.index),
    url(r'/back',views.back),
    url(r'/sensorscan',views.sensorscan),
    url(r'/scandata1',views.scandata1),
    url(r'/scandata3',views.scandata3),

    url(r'/scandata4', views.scandata4),
    url(r'/scandata5', views.scandata5),
    url(r'/scandata6', views.scandata6),

    url(r'/sensorrecord',views.sensorrecord),

]