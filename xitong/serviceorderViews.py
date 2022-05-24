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


#    定义添加会员服务的方法，响应页面请求
def tianjiaserviceorder(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回添加会员服务页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiaserviceorder.html',{'userall':userall,});


#  处理添加会员服务方法   
def tianjiaserviceorderact(request):

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

#  从页面post数据中获取价格   
    pricestr = request.POST.get("price");
    price = "";
    if(pricestr is not None):
        price = pricestr;

#  从页面post数据中获取订阅状态   
    substatestr = request.POST.get("substate");
    substate = "";
    if(substatestr is not None):
        substate = substatestr;

#  从页面post数据中获取收费方式   
    chargetypestr = request.POST.get("chargetype");
    chargetype = "";
    if(chargetypestr is not None):
        chargetype = chargetypestr;

#  从页面post数据中获取支付方式   
    paytypestr = request.POST.get("paytype");
    paytype = "";
    if(paytypestr is not None):
        paytype = paytypestr;

#  将会员服务的属性赋值给会员服务，生成会员服务对象   
    serviceorder = models.Serviceorder(user=user,userid=userid,price=price,substate=substate,chargetype=chargetype,paytype=paytype,);

#  调用save方法保存会员服务信息   
    serviceorder.save();



#  返回页面提示信息,添加会员服务成功,并跳转到会员服务管理页面   
    return HttpResponse(u"<script>alert('添加会员服务成功');window.location.href = '/serviceorder/serviceorderguanli';</script>");


#  定义表名管理方法，响应页面serviceorderguanli请求   
def serviceorderguanli(request):

#  通过all方法查询所有的会员服务信息   
    serviceorderall = models.Serviceorder.objects.all()



#  跳转到会员服务管理页面，并附带所有会员服务信息   
    return  render(request,'xitong/serviceorderguanli.html',{'serviceorderall':serviceorderall});


#  定义表名查看方法，响应页面serviceorderchakan请求   
def serviceorderchakan(request):

#  通过all方法查询所有的会员服务信息   
    serviceorderall = models.Serviceorder.objects.all()



#  跳转到会员服务查看页面，并附带所有会员服务信息   
    return  render(request,'xitong/serviceorderchakan.html',{'serviceorderall':serviceorderall});


#  定义修改会员服务方法，通过id查询对应的会员服务信息，返回页面展示  
def xiugaiserviceorder(request,id):

#  使用get方法，通过id查询对应的会员服务信息  
    serviceorder = models.Serviceorder.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改会员服务页面，并附带当前会员服务信息   
    return render(request, 'xitong/xiugaiserviceorder.html', {'serviceorder': serviceorder,'userall':userall,});


#  定义处理修改会员服务方法   
def xiugaiserviceorderact(request):

#  使用request获取post中的会员服务id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的会员服务id获取对应的会员服务信息   
    serviceorder = models.Serviceorder.objects.get(id=id);

#  从页面post数据中获取用户并赋值给serviceorder的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        serviceorder.user = userstr;

#  从页面post数据中获取用户id并赋值给serviceorder的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        serviceorder.userid = useridstr;

#  从页面post数据中获取价格并赋值给serviceorder的price字段   
    pricestr = request.POST.get("price");
    if(pricestr is not None):
        serviceorder.price = pricestr;

#  从页面post数据中获取订阅状态并赋值给serviceorder的substate字段   
    substatestr = request.POST.get("substate");
    if(substatestr is not None):
        serviceorder.substate = substatestr;

#  从页面post数据中获取收费方式并赋值给serviceorder的chargetype字段   
    chargetypestr = request.POST.get("chargetype");
    if(chargetypestr is not None):
        serviceorder.chargetype = chargetypestr;

#  从页面post数据中获取支付方式并赋值给serviceorder的paytype字段   
    paytypestr = request.POST.get("paytype");
    if(paytypestr is not None):
        serviceorder.paytype = paytypestr;

#  调用save方法保存会员服务信息   
    serviceorder.save();



#  返回页面提示信息,修改会员服务成功,并跳转到会员服务管理页面   
    return HttpResponse(u"<script>alert('修改会员服务成功');window.location.href = '/serviceorder/serviceorderguanli';</script>");


#  定义删除会员服务方法   
def shanchuserviceorderact(request,id):

#  调用django的delete方法，根据id删除会员服务信息   
    models.Serviceorder.objects.filter(id=id).delete();



#  返回页面提示信息,删除会员服务成功,并跳转到会员服务管理页面   
    return HttpResponse(u"<script>alert('删除会员服务成功');window.location.href = '/serviceorder/serviceorderguanli';</script>");


#  定义搜索会员服务方法，响应页面搜索请求   
def sousuoserviceorder(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的会员服务信息   
    serviceorderall = models.Serviceorder.objects.filter(user__icontains=search);

#  跳转到搜索会员服务页面，并附带查询的会员服务信息   
    return render(request, 'xitong/sousuoserviceorder.html', {"serviceorderall": serviceorderall});


#  处理会员服务详情   
def serviceorderxiangqing(request,id):

#  根据页面传入id获取会员服务信息   
    serviceorder = models.Serviceorder.objects.get(id=id);



#  跳转到会员服务详情页面,并会员服务信息传递到页面中   
    return render(request, 'xitong/serviceorderxiangqing.html', {"serviceorder": serviceorder});


#  定义跳转user添加会员服务页面的方法  
def usertianjiaserviceorder(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回user添加会员服务页面      
    return  render(request,'xitong/usertianjiaserviceorder.html',{'userall':userall,});


#  处理添加会员服务方法   
def usertianjiaserviceorderact(request):

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

#  从页面post数据中获取价格   
    pricestr = request.POST.get("price");
    price = "";
    if(pricestr is not None):
        price = pricestr;

#  从页面post数据中获取订阅状态   
    substatestr = request.POST.get("substate");
    substate = "";
    if(substatestr is not None):
        substate = substatestr;

#  从页面post数据中获取收费方式   
    chargetypestr = request.POST.get("chargetype");
    chargetype = "";
    if(chargetypestr is not None):
        chargetype = chargetypestr;

#  从页面post数据中获取支付方式   
    paytypestr = request.POST.get("paytype");
    paytype = "";
    if(paytypestr is not None):
        paytype = paytypestr;

#  将会员服务的属性赋值给会员服务，生成会员服务对象   
    serviceorder = models.Serviceorder(user=user,userid=userid,price=price,substate=substate,chargetype=chargetype,paytype=paytype,);

#  调用save方法保存会员服务信息   
    serviceorder.save();



#  返回页面提示信息,添加会员服务成功,并跳转到会员服务管理页面   
    return HttpResponse(u"<script>alert('添加会员服务成功');window.location.href = '/serviceorder/userserviceorderguanli';</script>");




#  跳转user会员服务管理页面      
def userserviceorderguanli(request):

#  查询出userid等于当前用户id的所有会员服务信息      
    serviceorderall = models.Serviceorder.objects.filter(userid=request.session["id"])



#  返回会员服务管理页面，并携带serviceorderall的数据信息      
    return  render(request,'xitong/userserviceorderguanli.html',{'serviceorderall':serviceorderall});


#  定义跳转user修改会员服务页面      
def userxiugaiserviceorder(request,id):

#  根据页面传入的会员服务id信息，查询出对应的会员服务信息      
    serviceorder = models.Serviceorder.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改会员服务页面，并携带查询出的会员服务信息      
    return render(request, 'xitong/userxiugaiserviceorder.html', {'serviceorder': serviceorder,'userall':userall,});


#  定义处理修改会员服务方法   
def userxiugaiserviceorderact(request):

#  使用request获取post中的会员服务id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的会员服务id获取对应的会员服务信息   
    serviceorder = models.Serviceorder.objects.get(id=id);

#  从页面post数据中获取用户并赋值给serviceorder的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        serviceorder.user = userstr;

#  从页面post数据中获取用户id并赋值给serviceorder的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        serviceorder.userid = useridstr;

#  从页面post数据中获取价格并赋值给serviceorder的price字段   
    pricestr = request.POST.get("price");
    if(pricestr is not None):
        serviceorder.price = pricestr;

#  从页面post数据中获取订阅状态并赋值给serviceorder的substate字段   
    substatestr = request.POST.get("substate");
    if(substatestr is not None):
        serviceorder.substate = substatestr;

#  从页面post数据中获取收费方式并赋值给serviceorder的chargetype字段   
    chargetypestr = request.POST.get("chargetype");
    if(chargetypestr is not None):
        serviceorder.chargetype = chargetypestr;

#  从页面post数据中获取支付方式并赋值给serviceorder的paytype字段   
    paytypestr = request.POST.get("paytype");
    if(paytypestr is not None):
        serviceorder.paytype = paytypestr;

#  调用save方法保存会员服务信息   
    serviceorder.save();



#  返回页面提示信息,修改会员服务成功,并跳转到会员服务管理页面   
    return HttpResponse(u"<script>alert('修改会员服务成功');window.location.href = '/serviceorder/userserviceorderguanli';</script>");




#  定义user删除会员服务信息     
def usershanchuserviceorderact(request,id):

#  根据页面传入的会员服务id信息，删除出对应的会员服务信息      
    models.Serviceorder.objects.filter(id=id).delete();



#  在页面给出提示信息，删除会员服务成功，并跳转到会员服务管理页面      
    return HttpResponse(u"<script>alert('删除会员服务成功');window.location.href = '/serviceorder/userserviceorderguanli';</script>");





