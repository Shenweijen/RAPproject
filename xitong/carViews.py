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


#    定义添加车辆的方法，响应页面请求
def tianjiacar(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回添加车辆页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiacar.html',{'userall':userall,});


#  处理添加车辆方法   
def tianjiacaract(request):

#  从页面post数据中获取车牌号   
    carnumberstr = request.POST.get("carnumber");
    carnumber = "";
    if(carnumberstr is not None):
        carnumber = carnumberstr;

#  从页面post数据中获取类别   
    typestr = request.POST.get("type");
    type = "";
    if(typestr is not None):
        type = typestr;

#  从页面post数据中获取厂商   
    firmstr = request.POST.get("firm");
    firm = "";
    if(firmstr is not None):
        firm = firmstr;

#  从页面post数据中获取车型   
    modelstr = request.POST.get("model");
    model = "";
    if(modelstr is not None):
        model = modelstr;

#  从页面post数据中获取车龄   
    caryearstr = request.POST.get("caryear");
    caryear = "";
    if(caryearstr is not None):
        caryear = caryearstr;

#  从页面post数据中获取颜色   
    colorstr = request.POST.get("color");
    color = "";
    if(colorstr is not None):
        color = colorstr;

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

#  将车辆的属性赋值给车辆，生成车辆对象   
    car = models.Car(carnumber=carnumber,type=type,firm=firm,model=model,caryear=caryear,color=color,user=user,userid=userid,);

#  调用save方法保存车辆信息   
    car.save();



#  返回页面提示信息,添加车辆成功,并跳转到车辆管理页面   
    return HttpResponse(u"<script>alert('添加车辆成功');window.location.href = '/car/carguanli';</script>");


#  定义表名管理方法，响应页面carguanli请求   
def carguanli(request):

#  通过all方法查询所有的车辆信息   
    carall = models.Car.objects.all()



#  跳转到车辆管理页面，并附带所有车辆信息   
    return  render(request,'xitong/carguanli.html',{'carall':carall});


#  定义表名查看方法，响应页面carchakan请求   
def carchakan(request):

#  通过all方法查询所有的车辆信息   
    carall = models.Car.objects.all()



#  跳转到车辆查看页面，并附带所有车辆信息   
    return  render(request,'xitong/carchakan.html',{'carall':carall});


#  定义修改车辆方法，通过id查询对应的车辆信息，返回页面展示  
def xiugaicar(request,id):

#  使用get方法，通过id查询对应的车辆信息  
    car = models.Car.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改车辆页面，并附带当前车辆信息   
    return render(request, 'xitong/xiugaicar.html', {'car': car,'userall':userall,});


#  定义处理修改车辆方法   
def xiugaicaract(request):

#  使用request获取post中的车辆id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的车辆id获取对应的车辆信息   
    car = models.Car.objects.get(id=id);

#  从页面post数据中获取车牌号并赋值给car的carnumber字段   
    carnumberstr = request.POST.get("carnumber");
    if(carnumberstr is not None):
        car.carnumber = carnumberstr;

#  从页面post数据中获取类别并赋值给car的type字段   
    typestr = request.POST.get("type");
    if(typestr is not None):
        car.type = typestr;

#  从页面post数据中获取厂商并赋值给car的firm字段   
    firmstr = request.POST.get("firm");
    if(firmstr is not None):
        car.firm = firmstr;

#  从页面post数据中获取车型并赋值给car的model字段   
    modelstr = request.POST.get("model");
    if(modelstr is not None):
        car.model = modelstr;

#  从页面post数据中获取车龄并赋值给car的caryear字段   
    caryearstr = request.POST.get("caryear");
    if(caryearstr is not None):
        car.caryear = caryearstr;

#  从页面post数据中获取颜色并赋值给car的color字段   
    colorstr = request.POST.get("color");
    if(colorstr is not None):
        car.color = colorstr;

#  从页面post数据中获取用户并赋值给car的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        car.user = userstr;

#  从页面post数据中获取用户id并赋值给car的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        car.userid = useridstr;

#  调用save方法保存车辆信息   
    car.save();



#  返回页面提示信息,修改车辆成功,并跳转到车辆管理页面   
    return HttpResponse(u"<script>alert('修改车辆成功');window.location.href = '/car/carguanli';</script>");


#  定义删除车辆方法   
def shanchucaract(request,id):

#  调用django的delete方法，根据id删除车辆信息   
    models.Car.objects.filter(id=id).delete();



#  返回页面提示信息,删除车辆成功,并跳转到车辆管理页面   
    return HttpResponse(u"<script>alert('删除车辆成功');window.location.href = '/car/carguanli';</script>");


#  定义搜索车辆方法，响应页面搜索请求   
def sousuocar(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的车辆信息   
    carall = models.Car.objects.filter(carnumber__icontains=search);

#  跳转到搜索车辆页面，并附带查询的车辆信息   
    return render(request, 'xitong/sousuocar.html', {"carall": carall});


#  处理车辆详情   
def carxiangqing(request,id):

#  根据页面传入id获取车辆信息   
    car = models.Car.objects.get(id=id);



#  跳转到车辆详情页面,并车辆信息传递到页面中   
    return render(request, 'xitong/carxiangqing.html', {"car": car});


#  定义跳转user添加车辆页面的方法  
def usertianjiacar(request):

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();



#  返回user添加车辆页面      
    return  render(request,'xitong/usertianjiacar.html',{'userall':userall,});


#  处理添加车辆方法   
def usertianjiacaract(request):

#  从页面post数据中获取车牌号   
    carnumberstr = request.POST.get("carnumber");
    carnumber = "";
    if(carnumberstr is not None):
        carnumber = carnumberstr;

#  从页面post数据中获取类别   
    typestr = request.POST.get("type");
    type = "";
    if(typestr is not None):
        type = typestr;

#  从页面post数据中获取厂商   
    firmstr = request.POST.get("firm");
    firm = "";
    if(firmstr is not None):
        firm = firmstr;

#  从页面post数据中获取车型   
    modelstr = request.POST.get("model");
    model = "";
    if(modelstr is not None):
        model = modelstr;

#  从页面post数据中获取车龄   
    caryearstr = request.POST.get("caryear");
    caryear = "";
    if(caryearstr is not None):
        caryear = caryearstr;

#  从页面post数据中获取颜色   
    colorstr = request.POST.get("color");
    color = "";
    if(colorstr is not None):
        color = colorstr;

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

#  将车辆的属性赋值给车辆，生成车辆对象   
    car = models.Car(carnumber=carnumber,type=type,firm=firm,model=model,caryear=caryear,color=color,user=user,userid=userid,);

#  调用save方法保存车辆信息   
    car.save();



#  返回页面提示信息,添加车辆成功,并跳转到车辆管理页面   
    return HttpResponse(u"<script>alert('添加车辆成功');window.location.href = '/car/usercarguanli';</script>");




#  跳转user车辆管理页面      
def usercarguanli(request):

#  查询出userid等于当前用户id的所有车辆信息      
    carall = models.Car.objects.filter(userid=request.session["id"])



#  返回车辆管理页面，并携带carall的数据信息      
    return  render(request,'xitong/usercarguanli.html',{'carall':carall});


#  定义跳转user修改车辆页面      
def userxiugaicar(request,id):

#  根据页面传入的车辆id信息，查询出对应的车辆信息      
    car = models.Car.objects.get(id=id);

#  获取页面数据user,使用DJANGO all方法查询所有数据   
    userall = models.User.objects.all();


#  跳转到修改车辆页面，并携带查询出的车辆信息      
    return render(request, 'xitong/userxiugaicar.html', {'car': car,'userall':userall,});


#  定义处理修改车辆方法   
def userxiugaicaract(request):

#  使用request获取post中的车辆id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的车辆id获取对应的车辆信息   
    car = models.Car.objects.get(id=id);

#  从页面post数据中获取车牌号并赋值给car的carnumber字段   
    carnumberstr = request.POST.get("carnumber");
    if(carnumberstr is not None):
        car.carnumber = carnumberstr;

#  从页面post数据中获取类别并赋值给car的type字段   
    typestr = request.POST.get("type");
    if(typestr is not None):
        car.type = typestr;

#  从页面post数据中获取厂商并赋值给car的firm字段   
    firmstr = request.POST.get("firm");
    if(firmstr is not None):
        car.firm = firmstr;

#  从页面post数据中获取车型并赋值给car的model字段   
    modelstr = request.POST.get("model");
    if(modelstr is not None):
        car.model = modelstr;

#  从页面post数据中获取车龄并赋值给car的caryear字段   
    caryearstr = request.POST.get("caryear");
    if(caryearstr is not None):
        car.caryear = caryearstr;

#  从页面post数据中获取颜色并赋值给car的color字段   
    colorstr = request.POST.get("color");
    if(colorstr is not None):
        car.color = colorstr;

#  从页面post数据中获取用户并赋值给car的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        car.user = userstr;

#  从页面post数据中获取用户id并赋值给car的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        car.userid = useridstr;

#  调用save方法保存车辆信息   
    car.save();



#  返回页面提示信息,修改车辆成功,并跳转到车辆管理页面   
    return HttpResponse(u"<script>alert('修改车辆成功');window.location.href = '/car/usercarguanli';</script>");




#  定义user删除车辆信息     
def usershanchucaract(request,id):

#  根据页面传入的车辆id信息，删除出对应的车辆信息      
    models.Car.objects.filter(id=id).delete();



#  在页面给出提示信息，删除车辆成功，并跳转到车辆管理页面      
    return HttpResponse(u"<script>alert('删除车辆成功');window.location.href = '/car/usercarguanli';</script>");





