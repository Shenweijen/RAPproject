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


#    定义添加维修工的方法，响应页面请求
def tianjiarepairman(request):



#  返回添加维修工页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiarepairman.html',{});


#  处理添加维修工方法   
def tianjiarepairmanact(request):

#  从页面post数据中获取姓名   
    namestr = request.POST.get("name");
    name = "";
    if(namestr is not None):
        name = namestr;

#  从页面post数据中获取用户名   
    usernamestr = request.POST.get("username");
    username = "";
    if(usernamestr is not None):
        username = usernamestr;

#  从页面post数据中获取密码   
    passwordstr = request.POST.get("password");
    password = "";
    if(passwordstr is not None):
        password = passwordstr;

#  从页面post数据中获取邮箱   
    emailstr = request.POST.get("email");
    email = "";
    if(emailstr is not None):
        email = emailstr;

#  从页面post数据中获取地址   
    addressstr = request.POST.get("address");
    address = "";
    if(addressstr is not None):
        address = addressstr;

#  从页面post数据中获取可救援类型   
    allowtypestr = request.POST.get("allowtype");
    allowtype = "";
    if(allowtypestr is not None):
        allowtype = allowtypestr;

#  从页面post数据中获取状态   
    statestr = request.POST.get("state");
    state = "";
    if(statestr is not None):
        state = statestr;

#  从页面post数据中获取银行卡   
    bankcardstr = request.POST.get("bankcard");
    bankcard = "";
    if(bankcardstr is not None):
        bankcard = bankcardstr;

#  从页面post数据中获取Payslip   
    payslipstr = request.POST.get("payslip");
    payslip = "";
    if(payslipstr is not None):
        payslip = payslipstr;

#  将维修工的属性赋值给维修工，生成维修工对象   
    repairman = models.Repairman(name=name,username=username,password=password,email=email,address=address,allowtype=allowtype,state=state,bankcard=bankcard,payslip=payslip,);

#  调用save方法保存维修工信息   
    repairman.save();



#  返回页面提示信息,添加维修工成功,并跳转到维修工管理页面   
    return HttpResponse(u"<script>alert('添加维修工成功');window.location.href = '/repairman/repairmanguanli';</script>");


#  定义表名管理方法，响应页面repairmanguanli请求   
def repairmanguanli(request):

#  通过all方法查询所有的维修工信息   
    repairmanall = models.Repairman.objects.all()



#  跳转到维修工管理页面，并附带所有维修工信息   
    return  render(request,'xitong/repairmanguanli.html',{'repairmanall':repairmanall});


#  定义表名查看方法，响应页面repairmanchakan请求   
def repairmanchakan(request):

#  通过all方法查询所有的维修工信息   
    repairmanall = models.Repairman.objects.all()



#  跳转到维修工查看页面，并附带所有维修工信息   
    return  render(request,'xitong/repairmanchakan.html',{'repairmanall':repairmanall});


#  定义修改维修工方法，通过id查询对应的维修工信息，返回页面展示  
def xiugairepairman(request,id):

#  使用get方法，通过id查询对应的维修工信息  
    repairman = models.Repairman.objects.get(id=id);


#  跳转到修改维修工页面，并附带当前维修工信息   
    return render(request, 'xitong/xiugairepairman.html', {'repairman': repairman,});


#  定义处理修改维修工方法   
def xiugairepairmanact(request):

#  使用request获取post中的维修工id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的维修工id获取对应的维修工信息   
    repairman = models.Repairman.objects.get(id=id);

#  从页面post数据中获取姓名并赋值给repairman的name字段   
    namestr = request.POST.get("name");
    if(namestr is not None):
        repairman.name = namestr;

#  从页面post数据中获取用户名并赋值给repairman的username字段   
    usernamestr = request.POST.get("username");
    if(usernamestr is not None):
        repairman.username = usernamestr;

#  从页面post数据中获取密码并赋值给repairman的password字段   
    passwordstr = request.POST.get("password");
    if(passwordstr is not None):
        repairman.password = passwordstr;

#  从页面post数据中获取邮箱并赋值给repairman的email字段   
    emailstr = request.POST.get("email");
    if(emailstr is not None):
        repairman.email = emailstr;

#  从页面post数据中获取地址并赋值给repairman的address字段   
    addressstr = request.POST.get("address");
    if(addressstr is not None):
        repairman.address = addressstr;

#  从页面post数据中获取可救援类型并赋值给repairman的allowtype字段   
    allowtypestr = request.POST.get("allowtype");
    if(allowtypestr is not None):
        repairman.allowtype = allowtypestr;

#  从页面post数据中获取状态并赋值给repairman的state字段   
    statestr = request.POST.get("state");
    if(statestr is not None):
        repairman.state = statestr;

#  从页面post数据中获取银行卡并赋值给repairman的bankcard字段   
    bankcardstr = request.POST.get("bankcard");
    if(bankcardstr is not None):
        repairman.bankcard = bankcardstr;

#  从页面post数据中获取Payslip并赋值给repairman的payslip字段   
    payslipstr = request.POST.get("payslip");
    if(payslipstr is not None):
        repairman.payslip = payslipstr;

#  调用save方法保存维修工信息   
    repairman.save();



#  返回页面提示信息,修改维修工成功,并跳转到维修工管理页面   
    return HttpResponse(u"<script>alert('修改维修工成功');window.location.href = '/repairman/repairmanguanli';</script>");


#  定义删除维修工方法   
def shanchurepairmanact(request,id):

#  调用django的delete方法，根据id删除维修工信息   
    models.Repairman.objects.filter(id=id).delete();



#  返回页面提示信息,删除维修工成功,并跳转到维修工管理页面   
    return HttpResponse(u"<script>alert('删除维修工成功');window.location.href = '/repairman/repairmanguanli';</script>");


#  定义搜索维修工方法，响应页面搜索请求   
def sousuorepairman(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的维修工信息   
    repairmanall = models.Repairman.objects.filter(name__icontains=search);

#  跳转到搜索维修工页面，并附带查询的维修工信息   
    return render(request, 'xitong/sousuorepairman.html', {"repairmanall": repairmanall});


#  处理维修工详情   
def repairmanxiangqing(request,id):

#  根据页面传入id获取维修工信息   
    repairman = models.Repairman.objects.get(id=id);



#  跳转到维修工详情页面,并维修工信息传递到页面中   
    return render(request, 'xitong/repairmanxiangqing.html', {"repairman": repairman});





