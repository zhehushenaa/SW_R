from django.shortcuts import render
from django.http import HttpResponse
from SW.gw import gw_model
from SW import models




def index(request):
    context={}
    context["hello"]='hello'
    return render(request,'indextest1.html',context)


def back(request):
    context={}
    context["hello"]='hello'
    return render(request,'back.html',context)

def sensorscan(request):
    context={}
    context["hello"]='hello'
    return render(request,'sensorscan.html')

def sensorrecord(request):
    context={}
    context["hello"]='hello'
    return render(request,'sensorrecord.html')


def scandata1(request):
    context={}
    # dataid=["20121","2001"]
    # datavalue = [21.5, 10]
    # g=gw_model()
    # datavalue=g.handle()
    # models.model_task.objects.create(task_name=hname, task_person=hperson, task_createtime=hcreatetime,
    #                                  task_endtime=hendtime, task_status=hstatus, task_describe=hdescribe)
    # data1 = models.model_sensor(SW_id="661", SW_num="20", SW_type="温度传感器", SW_power="56%", SW_status="正常")
    # data1.save()

    datavalue={'物联网控制柜':['20','X','0','X','220','8','X','X','20','正常','无'],
               '压力罐':['10','0.17','0','X','220','5','X','X','20','正常','无'],
               '水箱':['2','X','0','5','X','X','X','20','20','正常','无']}
               # '水泵机':['40','X','0','X','220','10','100','20','20','正常','无']}
    # datavalue={'物联网控制柜':['20','230']}

    print (datavalue)

    context["hello"]='hello'
    # data=["2020",22,""]
    return render(request,'scandata1.html',{'datavalue':datavalue})


def scandata3(request):
    context={}
    # dataid=["20121","2001"]
    # datavalue = [21.5, 10]
    try:
        g=gw_model()
        datavalue=g.handle()


    except:
        datavalue={"未收到数据":["未收到数据！","未收到数据","未收到数据！","未收到数据"]}

    print (datavalue)

    context["hello"]='hello'
    # data=["2020",22,""]
    return render(request,'scandata3.html',{'datavalue':datavalue})
    # return render(request,'scandata3.html',{'data':dataid)



def scandata4(request):
    context={}
    # dataid=["20121","2001"]
    # datavalue = [21.5, 10]
    # g=gw_model()
    # datavalue=g.handle()
    # print (datavalue)

    context["hello"]='hello'
    # data=["2020",22,""]
    return render(request,'scandata4.html')


def scandata5(request):
    context={}
    # dataid=["20121","2001"]
    # datavalue = [21.5, 10]
    # g=gw_model()
    # datavalue=g.handle()
    # print (datavalue)

    context["hello"]='hello'
    # data=["2020",22,""]
    return render(request,'scandata5.html')


def scandata6(request):
    context={}
    # dataid=["20121","2001"]
    # datavalue = [21.5, 10]
    # g=gw_model()
    # datavalue=g.handle()
    # print (datavalue)

    context["hello"]='hello'
    # data=["2020",22,""]
    return render(request,'scandata6.html')



# def update1(request):
#   print(request.POST)
#   # n1 = int(request.POST.get('n1'))
#   idb= str(request.POST.get('n2'))
#   sum = "我是出库的！变黄色！"
#   sjk_ys = sjk()
#   sjk_ys.update_0(idb)
#   # sjk_ys.close()
#   return HttpResponse(idb)