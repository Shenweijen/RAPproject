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


#    定义添加订单评价的方法，响应页面请求
def tianjiaordereval(request):

#  获取页面数据rescueorder,使用DJANGO all方法查询所有数据   
    rescueorderall = models.Rescueorder.objects.all();

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回添加订单评价页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiaordereval.html',{'rescueorderall':rescueorderall,'userall':userall,});


#  处理添加订单评价方法   
def tianjiaorderevalact(request):

#  从页面post数据中获取订单编号   
    rescueorderstr = request.POST.get("rescueorder");
    rescueorder = "";
    if(rescueorderstr is not None):
        rescueorder = rescueorderstr;

#  从页面post数据中获取订单id   
    rescueorderidstr = request.POST.get("rescueorderid");
    rescueorderid = "";
    if(rescueorderidstr is not None):
        rescueorderid = rescueorderidstr;

#  从页面post数据中获取内容   
    contentstr = request.POST.get("content");
    content = "";
    if(contentstr is not None):
        content = contentstr;

#  从页面post数据中获取评价时间   
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if(addtimestr is not None):
        addtime = addtimestr;

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

#  将订单评价的属性赋值给订单评价，生成订单评价对象   
    ordereval = models.Ordereval(rescueorder=rescueorder,rescueorderid=rescueorderid,content=content,addtime=addtime,user=user,userid=userid,);

#  调用save方法保存订单评价信息   
    ordereval.save();



#  返回页面提示信息,添加订单评价成功,并跳转到订单评价管理页面   
    return HttpResponse(u"<script>alert('添加订单评价成功');window.location.href = '/ordereval/orderevalguanli';</script>");


#  定义表名管理方法，响应页面orderevalguanli请求   
def orderevalguanli(request):

#  通过all方法查询所有的订单评价信息   
    orderevalall = models.Ordereval.objects.all()



#  跳转到订单评价管理页面，并附带所有订单评价信息   
    return  render(request,'xitong/orderevalguanli.html',{'orderevalall':orderevalall});


#  定义表名查看方法，响应页面orderevalchakan请求   
def orderevalchakan(request):

    rescueorderid = request.GET.get("rescueorderid");

    print(rescueorderid);

    if rescueorderid is not None:
        orderevalall = models.Ordereval.objects.filter(rescueorderid=rescueorderid);
    else:
        orderevalall = models.Ordereval.objects.all();

#  跳转到订单评价查看页面，并附带所有订单评价信息   
    return  render(request,'xitong/orderevalchakan.html',{'orderevalall':orderevalall});


#  定义修改订单评价方法，通过id查询对应的订单评价信息，返回页面展示  
def xiugaiordereval(request,id):

#  使用get方法，通过id查询对应的订单评价信息  
    ordereval = models.Ordereval.objects.get(id=id);

#  获取页面数据rescueorder,使用DJANGO all方法查询所有数据   
    rescueorderall = models.Rescueorder.objects.all();

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改订单评价页面，并附带当前订单评价信息   
    return render(request, 'xitong/xiugaiordereval.html', {'ordereval': ordereval,'rescueorderall':rescueorderall,'userall':userall,});


#  定义处理修改订单评价方法   
def xiugaiorderevalact(request):

#  使用request获取post中的订单评价id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的订单评价id获取对应的订单评价信息   
    ordereval = models.Ordereval.objects.get(id=id);

#  从页面post数据中获取订单编号并赋值给ordereval的rescueorder字段   
    rescueorderstr = request.POST.get("rescueorder");
    if(rescueorderstr is not None):
        ordereval.rescueorder = rescueorderstr;

#  从页面post数据中获取订单id并赋值给ordereval的rescueorderid字段   
    rescueorderidstr = request.POST.get("rescueorderid");
    if(rescueorderidstr is not None):
        ordereval.rescueorderid = rescueorderidstr;

#  从页面post数据中获取内容并赋值给ordereval的content字段   
    contentstr = request.POST.get("content");
    if(contentstr is not None):
        ordereval.content = contentstr;

#  从页面post数据中获取评价时间并赋值给ordereval的addtime字段   
    addtimestr = request.POST.get("addtime");
    if(addtimestr is not None):
        ordereval.addtime = addtimestr;

#  从页面post数据中获取用户并赋值给ordereval的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        ordereval.user = userstr;

#  从页面post数据中获取用户id并赋值给ordereval的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        ordereval.userid = useridstr;

#  调用save方法保存订单评价信息   
    ordereval.save();



#  返回页面提示信息,修改订单评价成功,并跳转到订单评价管理页面   
    return HttpResponse(u"<script>alert('修改订单评价成功');window.location.href = '/ordereval/orderevalguanli';</script>");


#  定义删除订单评价方法   
def shanchuorderevalact(request,id):

#  调用django的delete方法，根据id删除订单评价信息   
    models.Ordereval.objects.filter(id=id).delete();



#  返回页面提示信息,删除订单评价成功,并跳转到订单评价管理页面   
    return HttpResponse(u"<script>alert('删除订单评价成功');window.location.href = '/ordereval/orderevalguanli';</script>");


#  定义搜索订单评价方法，响应页面搜索请求   
def sousuoordereval(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的订单评价信息   
    orderevalall = models.Ordereval.objects.filter(rescueorder__icontains=search);

#  跳转到搜索订单评价页面，并附带查询的订单评价信息   
    return render(request, 'xitong/sousuoordereval.html', {"orderevalall": orderevalall});


#  处理订单评价详情   
def orderevalxiangqing(request,id):

#  根据页面传入id获取订单评价信息   
    ordereval = models.Ordereval.objects.get(id=id);



#  跳转到订单评价详情页面,并订单评价信息传递到页面中   
    return render(request, 'xitong/orderevalxiangqing.html', {"ordereval": ordereval});


#  定义跳转user添加订单评价页面的方法  
def usertianjiaordereval(request):

#  获取页面数据rescueorder,使用DJANGO all方法查询所有数据   
    rescueorderall = models.Rescueorder.objects.all();

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回user添加订单评价页面      
    return  render(request,'xitong/usertianjiaordereval.html',{'rescueorderall':rescueorderall,'userall':userall,});


#  处理添加订单评价方法   
def usertianjiaorderevalact(request):

#  从页面post数据中获取订单编号   
    rescueorderstr = request.POST.get("rescueorder");
    rescueorder = "";
    if(rescueorderstr is not None):
        rescueorder = rescueorderstr;

#  从页面post数据中获取订单id   
    rescueorderidstr = request.POST.get("rescueorderid");
    rescueorderid = "";
    if(rescueorderidstr is not None):
        rescueorderid = rescueorderidstr;

#  从页面post数据中获取内容   
    contentstr = request.POST.get("content");
    content = "";
    if(contentstr is not None):
        content = contentstr;

#  从页面post数据中获取评价时间   
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if(addtimestr is not None):
        addtime = addtimestr;

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

#  将订单评价的属性赋值给订单评价，生成订单评价对象   
    ordereval = models.Ordereval(rescueorder=rescueorder,rescueorderid=rescueorderid,content=content,addtime=addtime,user=user,userid=userid,);

#  调用save方法保存订单评价信息   
    ordereval.save();



#  返回页面提示信息,添加订单评价成功,并跳转到订单评价管理页面   
    return HttpResponse(u"<script>alert('添加订单评价成功');window.location.href = '/ordereval/userorderevalguanli';</script>");




#  跳转user订单评价管理页面      
def userorderevalguanli(request):

#  查询出userid等于当前用户id的所有订单评价信息      
    orderevalall = models.Ordereval.objects.filter(userid=request.session["id"])



#  返回订单评价管理页面，并携带orderevalall的数据信息      
    return  render(request,'xitong/userorderevalguanli.html',{'orderevalall':orderevalall});


#  定义跳转user修改订单评价页面      
def userxiugaiordereval(request,id):

#  根据页面传入的订单评价id信息，查询出对应的订单评价信息      
    ordereval = models.Ordereval.objects.get(id=id);

#  获取页面数据rescueorder,使用DJANGO all方法查询所有数据   
    rescueorderall = models.Rescueorder.objects.all();

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改订单评价页面，并携带查询出的订单评价信息      
    return render(request, 'xitong/userxiugaiordereval.html', {'ordereval': ordereval,'rescueorderall':rescueorderall,'userall':userall,});


#  定义处理修改订单评价方法   
def userxiugaiorderevalact(request):

#  使用request获取post中的订单评价id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的订单评价id获取对应的订单评价信息   
    ordereval = models.Ordereval.objects.get(id=id);

#  从页面post数据中获取订单编号并赋值给ordereval的rescueorder字段   
    rescueorderstr = request.POST.get("rescueorder");
    if(rescueorderstr is not None):
        ordereval.rescueorder = rescueorderstr;

#  从页面post数据中获取订单id并赋值给ordereval的rescueorderid字段   
    rescueorderidstr = request.POST.get("rescueorderid");
    if(rescueorderidstr is not None):
        ordereval.rescueorderid = rescueorderidstr;

#  从页面post数据中获取内容并赋值给ordereval的content字段   
    contentstr = request.POST.get("content");
    if(contentstr is not None):
        ordereval.content = contentstr;

#  从页面post数据中获取评价时间并赋值给ordereval的addtime字段   
    addtimestr = request.POST.get("addtime");
    if(addtimestr is not None):
        ordereval.addtime = addtimestr;

#  从页面post数据中获取用户并赋值给ordereval的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        ordereval.user = userstr;

#  从页面post数据中获取用户id并赋值给ordereval的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        ordereval.userid = useridstr;

#  调用save方法保存订单评价信息   
    ordereval.save();



#  返回页面提示信息,修改订单评价成功,并跳转到订单评价管理页面   
    return HttpResponse(u"<script>alert('修改订单评价成功');window.location.href = '/ordereval/userorderevalguanli';</script>");




#  定义user删除订单评价信息     
def usershanchuorderevalact(request,id):

#  根据页面传入的订单评价id信息，删除出对应的订单评价信息      
    models.Ordereval.objects.filter(id=id).delete();



#  在页面给出提示信息，删除订单评价成功，并跳转到订单评价管理页面      
    return HttpResponse(u"<script>alert('删除订单评价成功');window.location.href = '/ordereval/userorderevalguanli';</script>");





