
from django.shortcuts import render
from django.http import HttpResponse
from SW.gw import gw_model
from SW import models

# Create your tests here.
a={"Hu":["2","23","90"],"shen":["40","23","90"]}
for (key,value) in a.items():
    print(key)
    print(value[0])

data1 = models.model_sensor(SW_id="hu", SW_num="20", SW_type="温度传感器", SW_power="56%", SW_status="正常")
data1.save()
