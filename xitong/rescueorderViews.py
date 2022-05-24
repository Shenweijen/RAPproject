#coding:utf-8
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import random,os;



#  定义上传文件方法      
def uploadFile(request,filename):

#  获取传入的文件信息      
    file_obj = request.FILES.get(filename)

#  如果传入的文件为空，则返回false      
    if file_obj == None:
        return "false"

#  获取该文件的后缀信息      
    houzhui = file_obj.name.split(".")[-1];
    # 写入文件
    file_name = 'temp_file-%d' % random.randint(0, 100000) + "." + houzhui  # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join("static/upload/", file_name)
    dest = open(file_full_path, 'wb+')
    dest.write(file_obj.read())
    dest.close()

#  返回文件的名字      
    return file_name;


#    定义添加订单的方法，响应页面请求
def tianjiarescueorder(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();

#  获取页面数据car,使用DJANGO all方法查询所有数据   
    carall = models.Car.objects.all();

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();



#  返回添加订单页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiarescueorder.html',{'userall':userall,'carall':carall,'repairmanall':repairmanall,});


#  处理添加订单方法   
def tianjiarescueorderact(request):

#  从页面post数据中获取编号   
    ordernumberstr = request.POST.get("ordernumber");
    ordernumber = "";
    if(ordernumberstr is not None):
        ordernumber = ordernumberstr;

#  从页面post数据中获取用户   
    userstr = request.POST.get("user");
    user = "";
    if(userstr is not None):
        user = userstr;

#  从页面post数据中获取用户id   
    useridstr = request.POST.get("userid");
    userid = "";
    if(useridstr is not None):
        userid = useridstr;

#  从页面post数据中获取车辆   
    carstr = request.POST.get("car");
    car = "";
    if(carstr is not None):
        car = carstr;

#  从页面post数据中获取车辆id   
    caridstr = request.POST.get("carid");
    carid = "";
    if(caridstr is not None):
        carid = caridstr;

#  从页面post数据中获取问题类型   
    troubletypestr = request.POST.get("troubletype");
    troubletype = "";
    if(troubletypestr is not None):
        troubletype = troubletypestr;

#  从页面post数据中获取救援地址   
    rescaddressstr = request.POST.get("rescaddress");
    rescaddress = "";
    if(rescaddressstr is not None):
        rescaddress = rescaddressstr;

#  从页面post数据中获取问题描述   
    troubledescstr = request.POST.get("troubledesc");
    troubledesc = "";
    if(troubledescstr is not None):
        troubledesc = troubledescstr;

#  从页面post数据中获取救援原因   
    reasonstr = request.POST.get("reason");
    reason = "";
    if(reasonstr is not None):
        reason = reasonstr;

#  从页面post数据中获取状态   
    orderstatestr = request.POST.get("orderstate");
    orderstate = "";
    if(orderstatestr is not None):
        orderstate = orderstatestr;

#  从页面post数据中获取预估费用   
    precoststr = request.POST.get("precost");
    precost = "";
    if(precoststr is not None):
        precost = precoststr;

#  从页面post数据中获取预计救援时间   
    predatestr = request.POST.get("predate");
    predate = "";
    if(predatestr is not None):
        predate = predatestr;

#  从页面post数据中获取预计救援时长   
    durationstr = request.POST.get("duration");
    duration = "";
    if(durationstr is not None):
        duration = durationstr;

#  从页面post数据中获取维修工   
    repairmanstr = request.POST.get("repairman");
    repairman = "";
    if(repairmanstr is not None):
        repairman = repairmanstr;

#  从页面post数据中获取维修工id   
    repairmanidstr = request.POST.get("repairmanid");
    repairmanid = "";
    if(repairmanidstr is not None):
        repairmanid = repairmanidstr;

#  将订单的属性赋值给订单，生成订单对象   
    rescueorder = models.Rescueorder(ordernumber=ordernumber,user=user,userid=userid,car=car,carid=carid,troubletype=troubletype,rescaddress=rescaddress,troubledesc=troubledesc,reason=reason,orderstate=orderstate,precost=precost,predate=predate,duration=duration,repairman=repairman,repairmanid=repairmanid,);

#  调用save方法保存订单信息   
    rescueorder.save();



#  返回页面提示信息,添加订单成功,并跳转到订单管理页面   
    return HttpResponse(u"<script>alert('添加订单成功');window.location.href = '/rescueorder/rescueorderguanli';</script>");


#  定义表名管理方法，响应页面rescueorderguanli请求   
def rescueorderguanli(request):

#  通过all方法查询所有的订单信息   
    rescueorderall = models.Rescueorder.objects.all()



#  跳转到订单管理页面，并附带所有订单信息   
    return  render(request,'xitong/rescueorderguanli.html',{'rescueorderall':rescueorderall});


#  定义表名查看方法，响应页面rescueorderchakan请求   
def rescueorderchakan(request):

#  通过all方法查询所有的订单信息   
    rescueorderall = models.Rescueorder.objects.filter(orderstate='已审核');

#  跳转到订单查看页面，并附带所有订单信息   
    return  render(request,'xitong/rescueorderchakan.html',{'rescueorderall':rescueorderall});


#  定义表名查看方法，响应页面rescueorderchakan请求
def repairmanrescueorderchakan(request):

#  通过all方法查询所有的订单信息
    rescueorderall = models.Rescueorder.objects.filter(repairmanid=request.session["id"]);

#  跳转到订单查看页面，并附带所有订单信息
    return  render(request,'xitong/repairmanrescueorderchakan.html',{'rescueorderall':rescueorderall});



#  定义修改订单方法，通过id查询对应的订单信息，返回页面展示  
def xiugairescueorder(request,id):

#  使用get方法，通过id查询对应的订单信息  
    rescueorder = models.Rescueorder.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();

#  获取页面数据car,使用DJANGO all方法查询所有数据   
    carall = models.Car.objects.all();

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();


#  跳转到修改订单页面，并附带当前订单信息   
    return render(request, 'xitong/xiugairescueorder.html', {'rescueorder': rescueorder,'userall':userall,'carall':carall,'repairmanall':repairmanall,});


#  定义处理修改订单方法   
def xiugairescueorderact(request):

#  使用request获取post中的订单id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的订单id获取对应的订单信息   
    rescueorder = models.Rescueorder.objects.get(id=id);

#  从页面post数据中获取编号并赋值给rescueorder的ordernumber字段   
    ordernumberstr = request.POST.get("ordernumber");
    if(ordernumberstr is not None):
        rescueorder.ordernumber = ordernumberstr;

#  从页面post数据中获取用户并赋值给rescueorder的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        rescueorder.user = userstr;

#  从页面post数据中获取用户id并赋值给rescueorder的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        rescueorder.userid = useridstr;

#  从页面post数据中获取车辆并赋值给rescueorder的car字段   
    carstr = request.POST.get("car");
    if(carstr is not None):
        rescueorder.car = carstr;

#  从页面post数据中获取车辆id并赋值给rescueorder的carid字段   
    caridstr = request.POST.get("carid");
    if(caridstr is not None):
        rescueorder.carid = caridstr;

#  从页面post数据中获取问题类型并赋值给rescueorder的troubletype字段   
    troubletypestr = request.POST.get("troubletype");
    if(troubletypestr is not None):
        rescueorder.troubletype = troubletypestr;

#  从页面post数据中获取救援地址并赋值给rescueorder的rescaddress字段   
    rescaddressstr = request.POST.get("rescaddress");
    if(rescaddressstr is not None):
        rescueorder.rescaddress = rescaddressstr;

#  从页面post数据中获取问题描述并赋值给rescueorder的troubledesc字段   
    troubledescstr = request.POST.get("troubledesc");
    if(troubledescstr is not None):
        rescueorder.troubledesc = troubledescstr;

#  从页面post数据中获取救援原因并赋值给rescueorder的reason字段   
    reasonstr = request.POST.get("reason");
    if(reasonstr is not None):
        rescueorder.reason = reasonstr;

#  从页面post数据中获取状态并赋值给rescueorder的orderstate字段   
    orderstatestr = request.POST.get("orderstate");
    if(orderstatestr is not None):
        rescueorder.orderstate = orderstatestr;

#  从页面post数据中获取预估费用并赋值给rescueorder的precost字段   
    precoststr = request.POST.get("precost");
    if(precoststr is not None):
        rescueorder.precost = precoststr;

#  从页面post数据中获取预计救援时间并赋值给rescueorder的predate字段   
    predatestr = request.POST.get("predate");
    if(predatestr is not None):
        rescueorder.predate = predatestr;

#  从页面post数据中获取预计救援时长并赋值给rescueorder的duration字段   
    durationstr = request.POST.get("duration");
    if(durationstr is not None):
        rescueorder.duration = durationstr;

#  从页面post数据中获取维修工并赋值给rescueorder的repairman字段   
    repairmanstr = request.POST.get("repairman");
    if(repairmanstr is not None):
        rescueorder.repairman = repairmanstr;

#  从页面post数据中获取维修工id并赋值给rescueorder的repairmanid字段   
    repairmanidstr = request.POST.get("repairmanid");
    if(repairmanidstr is not None):
        rescueorder.repairmanid = repairmanidstr;

#  调用save方法保存订单信息   
    rescueorder.save();



#  返回页面提示信息,修改订单成功,并跳转到订单管理页面   
    return HttpResponse(u"<script>alert('修改订单成功');window.location.href = '/rescueorder/rescueorderguanli';</script>");


#  定义删除订单方法   
def shanchurescueorderact(request,id):

#  调用django的delete方法，根据id删除订单信息   
    models.Rescueorder.objects.filter(id=id).delete();

#  返回页面提示信息,删除订单成功,并跳转到订单管理页面   
    return HttpResponse(u"<script>alert('删除订单成功');window.location.href = '/rescueorder/rescueorderguanli';</script>");



def wancheng(request,id):

    rescueorder = models.Rescueorder.objects.get(id=id);

    rescueorder.orderstate = "已完成";

    rescueorder.save();

#  返回页面提示信息,删除订单成功,并跳转到订单管理页面
    return HttpResponse(u"<script>alert('订单完成成功');window.location.href = '/rescueorder/userrescueorderguanli';</script>");

def tongguo(request,id):

    rescueorder = models.Rescueorder.objects.get(id=id);

    rescueorder.orderstate = "已审核";

    rescueorder.save();

#  返回页面提示信息,删除订单成功,并跳转到订单管理页面
    return HttpResponse(u"<script>alert('订单审核完成');window.location.href = '/rescueorder/rescueorderguanli';</script>");

def jiedan(request,id):

    rescueorder = models.Rescueorder.objects.get(id=id);

    rescueorder.orderstate = "已接单";

    rescueorder.repairman = request.session["mingzi"];
    rescueorder.repairmanid = request.session["id"];

    rescueorder.save();

#  返回页面提示信息,删除订单成功,并跳转到订单管理页面
    return HttpResponse(u"<script>alert('接单成功');window.location.href = '/rescueorder/rescueorderchakan';</script>");


#  定义搜索订单方法，响应页面搜索请求   
def sousuorescueorder(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的订单信息   
    rescueorderall = models.Rescueorder.objects.filter(ordernumber__icontains=search);

#  跳转到搜索订单页面，并附带查询的订单信息   
    return render(request, 'xitong/sousuorescueorder.html', {"rescueorderall": rescueorderall});


#  处理订单详情   
def rescueorderxiangqing(request,id):

#  根据页面传入id获取订单信息   
    rescueorder = models.Rescueorder.objects.get(id=id);



#  跳转到订单详情页面,并订单信息传递到页面中   
    return render(request, 'xitong/rescueorderxiangqing.html', {"rescueorder": rescueorder});


#  定义跳转user添加订单页面的方法  
def usertianjiarescueorder(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();

#  获取页面数据car,使用DJANGO all方法查询所有数据   
    carall = models.Car.objects.filter(userid=request.session["id"]);

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();


#  返回user添加订单页面      
    return  render(request,'xitong/usertianjiarescueorder.html',{'userall':userall,'carall':carall,'repairmanall':repairmanall,});


#  处理添加订单方法   
def usertianjiarescueorderact(request):

#  从页面post数据中获取编号   
    ordernumberstr = request.POST.get("ordernumber");
    ordernumber = "";
    if(ordernumberstr is not None):
        ordernumber = ordernumberstr;

#  从页面post数据中获取用户   
    userstr = request.POST.get("user");
    user = "";
    if(userstr is not None):
        user = userstr;

#  从页面post数据中获取用户id   
    useridstr = request.POST.get("userid");
    userid = "";
    if(useridstr is not None):
        userid = useridstr;

#  从页面post数据中获取车辆   
    carstr = request.POST.get("car");
    car = "";
    if(carstr is not None):
        car = carstr;

#  从页面post数据中获取车辆id   
    caridstr = request.POST.get("carid");
    carid = "";
    if(caridstr is not None):
        carid = caridstr;

#  从页面post数据中获取问题类型   
    troubletypestr = request.POST.get("troubletype");
    troubletype = "";
    if(troubletypestr is not None):
        troubletype = troubletypestr;

#  从页面post数据中获取救援地址   
    rescaddressstr = request.POST.get("rescaddress");
    rescaddress = "";
    if(rescaddressstr is not None):
        rescaddress = rescaddressstr;

#  从页面post数据中获取问题描述   
    troubledescstr = request.POST.get("troubledesc");
    troubledesc = "";
    if(troubledescstr is not None):
        troubledesc = troubledescstr;

#  从页面post数据中获取救援原因   
    reasonstr = request.POST.get("reason");
    reason = "";
    if(reasonstr is not None):
        reason = reasonstr;

#  从页面post数据中获取状态   
    orderstatestr = request.POST.get("orderstate");
    orderstate = "";
    if(orderstatestr is not None):
        orderstate = orderstatestr;

#  从页面post数据中获取预估费用   
    precoststr = request.POST.get("precost");
    precost = "";
    if(precoststr is not None):
        precost = precoststr;

#  从页面post数据中获取预计救援时间   
    predatestr = request.POST.get("predate");
    predate = "";
    if(predatestr is not None):
        predate = predatestr;

#  从页面post数据中获取预计救援时长   
    durationstr = request.POST.get("duration");
    duration = "";
    if(durationstr is not None):
        duration = durationstr;

#  从页面post数据中获取维修工   
    repairmanstr = request.POST.get("repairman");
    repairman = "";
    if(repairmanstr is not None):
        repairman = repairmanstr;

#  从页面post数据中获取维修工id   
    repairmanidstr = request.POST.get("repairmanid");
    repairmanid = "";
    if(repairmanidstr is not None):
        repairmanid = repairmanidstr;


    repairman = "未接单";
    repairmanid = -1;

#  将订单的属性赋值给订单，生成订单对象   
    rescueorder = models.Rescueorder(ordernumber=ordernumber,user=user,userid=userid,car=car,carid=carid,troubletype=troubletype,rescaddress=rescaddress,troubledesc=troubledesc,reason=reason,orderstate=orderstate,precost=precost,predate=predate,duration=duration,repairman=repairman,repairmanid=repairmanid,);

#  调用save方法保存订单信息   
    rescueorder.save();



#  返回页面提示信息,添加订单成功,并跳转到订单管理页面   
    return HttpResponse(u"<script>alert('添加订单成功');window.location.href = '/rescueorder/userrescueorderguanli';</script>");




#  跳转user订单管理页面      
def userrescueorderguanli(request):

#  查询出userid等于当前用户id的所有订单信息      
    rescueorderall = models.Rescueorder.objects.filter(userid=request.session["id"])



#  返回订单管理页面，并携带rescueorderall的数据信息      
    return  render(request,'xitong/userrescueorderguanli.html',{'rescueorderall':rescueorderall});


#  定义跳转user修改订单页面      
def userxiugairescueorder(request,id):

#  根据页面传入的订单id信息，查询出对应的订单信息      
    rescueorder = models.Rescueorder.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();

#  获取页面数据car,使用DJANGO all方法查询所有数据   
    carall = models.Car.objects.all();

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();


#  跳转到修改订单页面，并携带查询出的订单信息      
    return render(request, 'xitong/userxiugairescueorder.html', {'rescueorder': rescueorder,'userall':userall,'carall':carall,'repairmanall':repairmanall,});


#  定义处理修改订单方法   
def userxiugairescueorderact(request):

#  使用request获取post中的订单id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的订单id获取对应的订单信息   
    rescueorder = models.Rescueorder.objects.get(id=id);

#  从页面post数据中获取编号并赋值给rescueorder的ordernumber字段   
    ordernumberstr = request.POST.get("ordernumber");
    if(ordernumberstr is not None):
        rescueorder.ordernumber = ordernumberstr;

#  从页面post数据中获取用户并赋值给rescueorder的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        rescueorder.user = userstr;

#  从页面post数据中获取用户id并赋值给rescueorder的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        rescueorder.userid = useridstr;

#  从页面post数据中获取车辆并赋值给rescueorder的car字段   
    carstr = request.POST.get("car");
    if(carstr is not None):
        rescueorder.car = carstr;

#  从页面post数据中获取车辆id并赋值给rescueorder的carid字段   
    caridstr = request.POST.get("carid");
    if(caridstr is not None):
        rescueorder.carid = caridstr;

#  从页面post数据中获取问题类型并赋值给rescueorder的troubletype字段   
    troubletypestr = request.POST.get("troubletype");
    if(troubletypestr is not None):
        rescueorder.troubletype = troubletypestr;

#  从页面post数据中获取救援地址并赋值给rescueorder的rescaddress字段   
    rescaddressstr = request.POST.get("rescaddress");
    if(rescaddressstr is not None):
        rescueorder.rescaddress = rescaddressstr;

#  从页面post数据中获取问题描述并赋值给rescueorder的troubledesc字段   
    troubledescstr = request.POST.get("troubledesc");
    if(troubledescstr is not None):
        rescueorder.troubledesc = troubledescstr;

#  从页面post数据中获取救援原因并赋值给rescueorder的reason字段   
    reasonstr = request.POST.get("reason");
    if(reasonstr is not None):
        rescueorder.reason = reasonstr;

#  从页面post数据中获取状态并赋值给rescueorder的orderstate字段   
    orderstatestr = request.POST.get("orderstate");
    if(orderstatestr is not None):
        rescueorder.orderstate = orderstatestr;

#  从页面post数据中获取预估费用并赋值给rescueorder的precost字段   
    precoststr = request.POST.get("precost");
    if(precoststr is not None):
        rescueorder.precost = precoststr;

#  从页面post数据中获取预计救援时间并赋值给rescueorder的predate字段   
    predatestr = request.POST.get("predate");
    if(predatestr is not None):
        rescueorder.predate = predatestr;

#  从页面post数据中获取预计救援时长并赋值给rescueorder的duration字段   
    durationstr = request.POST.get("duration");
    if(durationstr is not None):
        rescueorder.duration = durationstr;

#  从页面post数据中获取维修工并赋值给rescueorder的repairman字段   
    repairmanstr = request.POST.get("repairman");
    if(repairmanstr is not None):
        rescueorder.repairman = repairmanstr;

#  从页面post数据中获取维修工id并赋值给rescueorder的repairmanid字段   
    repairmanidstr = request.POST.get("repairmanid");
    if(repairmanidstr is not None):
        rescueorder.repairmanid = repairmanidstr;

#  调用save方法保存订单信息   
    rescueorder.save();



#  返回页面提示信息,修改订单成功,并跳转到订单管理页面   
    return HttpResponse(u"<script>alert('修改订单成功');window.location.href = '/rescueorder/userrescueorderguanli';</script>");




#  定义user删除订单信息     
def usershanchurescueorderact(request,id):

#  根据页面传入的订单id信息，删除出对应的订单信息      
    models.Rescueorder.objects.filter(id=id).delete();



#  在页面给出提示信息，删除订单成功，并跳转到订单管理页面      
    return HttpResponse(u"<script>alert('删除订单成功');window.location.href = '/rescueorder/userrescueorderguanli';</script>");





