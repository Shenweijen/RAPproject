#coding:utf-8
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import datetime,os,json,random


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


#  定义跳转到登录页面的方法    
def login(request):

#  返回登录页面    
    return render(request, 'xitong/login.html');



#  定义跳转到注册页面的方法    
def regist(request):

#  返回注册页面    
    return render(request, 'xitong/regist.html');



#  定义登录方法     
def loginact(request):

#  从POST中获取username     
    username = request.POST["username"];

#  从POST中获取password     
    password = request.POST["password"];

#  从POST中获取shenfen     
    shenfen = request.POST["shenfen"];

#  如果当前登录身份为管理员    
    if(shenfen == 'Admin'):

#  从admin查询是否有账号面与用户输入一直的管理员信息    
        admins = models.Admin.objects.filter(username=username, password=password);

#  如果查询出的数量大于0    
        if (admins.count() > 0):

#  将登录用户的信息保存到session中    
            request.session["shenfen"] = shenfen;

#  获取当前登录管理员的id信息    
            request.session["id"] = admins[0].id;

#  获取当前登录管理员的mingzi信息    
            request.session["mingzi"] = admins[0].name;

#  获取登录管理员的管理员id信息，并赋值给session的id字段    
            request.session["id"] = admins[0].id;

#  获取登录管理员的姓名信息，并赋值给session的name字段    
            request.session["name"] = admins[0].name;

#  获取登录管理员的用户名信息，并赋值给session的username字段    
            request.session["username"] = admins[0].username;

#  获取登录管理员的密码信息，并赋值给session的password字段    
            request.session["password"] = admins[0].password;

#  获取登录管理员的邮箱信息，并赋值给session的email字段    
            request.session["email"] = admins[0].email;

#  获取登录管理员的管理区域信息，并赋值给session的managearea字段    
            request.session["managearea"] = admins[0].managearea;

#  跳转到管理员个人中心    
            return render(request, 'xitong/adminindex.html');

#  给出页面提示用户名或密码错误，并跳转到登录页面    
        return HttpResponse(u"<script>alert('Account or Password is wrong');window.location.href = '/loginAndRegist/login';</script>");

#  如果当前登录身份为用户    
    if(shenfen == 'User'):

#  从user查询是否有账号面与用户输入一直的用户信息    
        users = models.User.objects.filter(username=username, password=password);

#  如果查询出的数量大于0    
        if (users.count() > 0):

#  将登录用户的信息保存到session中    
            request.session["shenfen"] = shenfen;

#  获取当前登录用户的id信息    
            request.session["id"] = users[0].id;

#  获取当前登录用户的mingzi信息    
            request.session["mingzi"] = users[0].name;

#  获取登录用户的用户id信息，并赋值给session的id字段    
            request.session["id"] = users[0].id;

#  获取登录用户的姓名信息，并赋值给session的name字段    
            request.session["name"] = users[0].name;

#  获取登录用户的用户名信息，并赋值给session的username字段    
            request.session["username"] = users[0].username;

#  获取登录用户的密码信息，并赋值给session的password字段    
            request.session["password"] = users[0].password;

#  获取登录用户的出生日期信息，并赋值给session的birthday字段    
            request.session["birthday"] = users[0].birthday;

#  获取登录用户的性别信息，并赋值给session的sex字段    
            request.session["sex"] = users[0].sex;

#  获取登录用户的邮箱信息，并赋值给session的email字段    
            request.session["email"] = users[0].email;

#  获取登录用户的住址信息，并赋值给session的homeaddress字段    
            request.session["homeaddress"] = users[0].homeaddress;

#  获取登录用户的紧急联系人信息，并赋值给session的emercontact字段    
            request.session["emercontact"] = users[0].emercontact;

#  获取登录用户的银行卡信息，并赋值给session的bankcard字段    
            request.session["bankcard"] = users[0].bankcard;

#  获取登录用户的Payslip信息，并赋值给session的payslip字段    
            request.session["payslip"] = users[0].payslip;

#  跳转到用户个人中心    
            return render(request, 'xitong/userindex.html');

#  给出页面提示用户名或密码错误，并跳转到登录页面    
        return HttpResponse(u"<script>alert('Account or Password is wrong');window.location.href = '/loginAndRegist/login';</script>");

#  如果当前登录身份为维修工    
    if(shenfen == 'RAP'):

#  从repairman查询是否有账号面与用户输入一直的维修工信息    
        repairmans = models.Repairman.objects.filter(username=username, password=password);

#  如果查询出的数量大于0    
        if (repairmans.count() > 0):

#  将登录用户的信息保存到session中    
            request.session["shenfen"] = shenfen;

#  获取当前登录维修工的id信息    
            request.session["id"] = repairmans[0].id;

#  获取当前登录维修工的mingzi信息    
            request.session["mingzi"] = repairmans[0].name;

#  获取登录维修工的维修工id信息，并赋值给session的id字段    
            request.session["id"] = repairmans[0].id;

#  获取登录维修工的姓名信息，并赋值给session的name字段    
            request.session["name"] = repairmans[0].name;

#  获取登录维修工的用户名信息，并赋值给session的username字段    
            request.session["username"] = repairmans[0].username;

#  获取登录维修工的密码信息，并赋值给session的password字段    
            request.session["password"] = repairmans[0].password;

#  获取登录维修工的邮箱信息，并赋值给session的email字段    
            request.session["email"] = repairmans[0].email;

#  获取登录维修工的地址信息，并赋值给session的address字段    
            request.session["address"] = repairmans[0].address;

#  获取登录维修工的可救援类型信息，并赋值给session的allowtype字段    
            request.session["allowtype"] = repairmans[0].allowtype;

#  获取登录维修工的状态信息，并赋值给session的state字段    
            request.session["state"] = repairmans[0].state;

#  获取登录维修工的银行卡信息，并赋值给session的bankcard字段    
            request.session["bankcard"] = repairmans[0].bankcard;

#  获取登录维修工的Payslip信息，并赋值给session的payslip字段    
            request.session["payslip"] = repairmans[0].payslip;

#  跳转到维修工个人中心    
            return render(request, 'xitong/repairmanindex.html');

#  给出页面提示用户名或密码错误，并跳转到登录页面    
        return HttpResponse(u"<script>alert('Account or Password is wrong');window.location.href = '/loginAndRegist/login';</script>");

#  给出页面提示请选择登录身份，并跳转到登录页面    
    return HttpResponse(u"<script>alert('Choose Identity');window.location.href = '/loginAndRegist/login';</script>");



#  定义注册方法     
def registact(request):

#  从POST中获取username参数     
    username = request.POST["username"];

#  从POST中获取password参数     
    password = request.POST["password"];

#  从POST中获取shenfen参数     
    shenfen = request.POST["shenfen"];

#  从POST中获取repassword参数     
    repassword = request.POST["repassword"];

#  如果password与repassword不一致     
    if(password != repassword):

#  返回两次密码不一致的提示信息，并返回登录页面     
        return HttpResponse(u"<script>alert('Password does not match');window.location.href = '/loginAndRegist/login';</script>");

#  如果当前注册身份为管理员    
    if(shenfen == 'Admin'):

#  根据页面传入的username信息，查询系统中的管理员信息    
        admins = models.Admin.objects.filter(username=username);

#  如果数据数量大于0    
        if(admins.count() > 0):

#  给出用户提示该账号已存在，并跳转到注册页面    
                return HttpResponse(u"<script>alert('Account exist!');window.location.href = '/loginAndRegist/regist';</script>");
        else:

#  将传入的管理员信息保存到admin表中    
            admin = models.Admin(username=username,password=password);
            admin.save();

#  给出用户提示注册成功，并跳转到登录页面    
            return HttpResponse(u"<script>alert('Register complete!');window.location.href = '/loginAndRegist/login/';</script>");

#  如果当前注册身份为用户    
    if(shenfen == 'User'):

#  根据页面传入的username信息，查询系统中的用户信息    
        users = models.User.objects.filter(username=username);

#  如果数据数量大于0    
        if(users.count() > 0):

#  给出用户提示该账号已存在，并跳转到注册页面    
                return HttpResponse(u"<script>alert('Account exist!');window.location.href = '/loginAndRegist/regist';</script>");
        else:

#  将传入的用户信息保存到user表中    
            user = models.User(username=username,password=password,name='User');
            user.save();

#  给出用户提示注册成功，并跳转到登录页面    
            return HttpResponse(u"<script>alert('Register complete!');window.location.href = '/loginAndRegist/login/';</script>");

#  如果当前注册身份为维修工    
    if(shenfen == 'RAP'):

#  根据页面传入的username信息，查询系统中的维修工信息    
        repairmans = models.Repairman.objects.filter(username=username);

#  如果数据数量大于0    
        if(repairmans.count() > 0):

#  给出用户提示该账号已存在，并跳转到注册页面    
                return HttpResponse(u"<script>alert('Account exist!');window.location.href = '/loginAndRegist/regist';</script>");
        else:

#  将传入的维修工信息保存到repairman表中    
            repairman = models.Repairman(username=username,password=password,name='RAP');
            repairman.save();

#  给出用户提示注册成功，并跳转到登录页面    
            return HttpResponse(u"<script>alert('Register complete');window.location.href = '/loginAndRegist/login/';</script>");

#  给出页面提示请选择注册身份，并跳转到注册页面    
    return HttpResponse(u"<script>alert('Choose Identity');window.location.href = '/loginAndRegist/regist';</script>");



#  定义退出系统方法    
def tuichuxitong(request):

#  清除用户session信息   
    request.session.clear();

#  返回系统登录页面   
    return render(request, 'xitong/login.html');



#  定义跳转管理员个人中心    
def adminindex(request):

#  返回管理员个人中心页面    
    return render(request, 'xitong/adminindex.html');



#  定义跳转用户个人中心    
def userindex(request):

#  返回用户个人中心页面    
    return render(request, 'xitong/userindex.html');



#  定义跳转维修工个人中心    
def repairmanindex(request):

#  返回维修工个人中心页面    
    return render(request, 'xitong/repairmanindex.html');



#  定义处理管理员修改个人信息的方法    
def adminxiugaigerenxinxiact(request):

#  获取需要修改的管理员id信息    
    id = request.POST.get("id");

#  根据传入的管理员id信息使用get方法获取管理员信息    
    admin = models.Admin.objects.get(id=id);

#  从POST中获取管理员id信息，并赋值给admin的id字段    
    admin.id = request.POST.get("id");

#  从POST中获取管理员id信息，并赋值给session的id字段    
    request.session['id'] = request.POST.get("id");

#  从POST中获取姓名信息，并赋值给admin的name字段    
    admin.name = request.POST.get("name");

#  从POST中获取姓名信息，并赋值给session的name字段    
    request.session['name'] = request.POST.get("name");

#  从POST中获取用户名信息，并赋值给admin的username字段    
    admin.username = request.POST.get("username");

#  从POST中获取用户名信息，并赋值给session的username字段    
    request.session['username'] = request.POST.get("username");

#  从POST中获取密码信息，并赋值给admin的password字段    
    admin.password = request.POST.get("password");

#  从POST中获取密码信息，并赋值给session的password字段    
    request.session['password'] = request.POST.get("password");

#  从POST中获取邮箱信息，并赋值给admin的email字段    
    admin.email = request.POST.get("email");

#  从POST中获取邮箱信息，并赋值给session的email字段    
    request.session['email'] = request.POST.get("email");

#  从POST中获取管理区域信息，并赋值给admin的managearea字段    
    admin.managearea = request.POST.get("managearea");

#  从POST中获取管理区域信息，并赋值给session的managearea字段    
    request.session['managearea'] = request.POST.get("managearea");

#  使用save方法保存管理员信息    
    admin.save();

#  给出页面提示修改成功，并跳转到管理员个人中心    
    return HttpResponse(u"<script>alert('Change successful!');window.location.href = '/loginAndRegist/adminindex';</script>");

#  定义处理用户修改个人信息的方法    
def userxiugaigerenxinxiact(request):

#  获取需要修改的用户id信息    
    id = request.POST.get("id");

#  根据传入的用户id信息使用get方法获取用户信息    
    user = models.User.objects.get(id=id);

#  从POST中获取用户id信息，并赋值给user的id字段    
    user.id = request.POST.get("id");

#  从POST中获取用户id信息，并赋值给session的id字段    
    request.session['id'] = request.POST.get("id");

#  从POST中获取姓名信息，并赋值给user的name字段    
    user.name = request.POST.get("name");

#  从POST中获取姓名信息，并赋值给session的name字段    
    request.session['name'] = request.POST.get("name");

#  从POST中获取用户名信息，并赋值给user的username字段    
    user.username = request.POST.get("username");

#  从POST中获取用户名信息，并赋值给session的username字段    
    request.session['username'] = request.POST.get("username");

#  从POST中获取密码信息，并赋值给user的password字段    
    user.password = request.POST.get("password");

#  从POST中获取密码信息，并赋值给session的password字段    
    request.session['password'] = request.POST.get("password");

#  从POST中获取出生日期信息，并赋值给user的birthday字段    
    user.birthday = request.POST.get("birthday");

#  从POST中获取出生日期信息，并赋值给session的birthday字段    
    request.session['birthday'] = request.POST.get("birthday");

#  从POST中获取性别信息，并赋值给user的sex字段    
    user.sex = request.POST.get("sex");

#  从POST中获取性别信息，并赋值给session的sex字段    
    request.session['sex'] = request.POST.get("sex");

#  从POST中获取邮箱信息，并赋值给user的email字段    
    user.email = request.POST.get("email");

#  从POST中获取邮箱信息，并赋值给session的email字段    
    request.session['email'] = request.POST.get("email");

#  从POST中获取住址信息，并赋值给user的homeaddress字段    
    user.homeaddress = request.POST.get("homeaddress");

#  从POST中获取住址信息，并赋值给session的homeaddress字段    
    request.session['homeaddress'] = request.POST.get("homeaddress");

#  从POST中获取紧急联系人信息，并赋值给user的emercontact字段    
    user.emercontact = request.POST.get("emercontact");

#  从POST中获取紧急联系人信息，并赋值给session的emercontact字段    
    request.session['emercontact'] = request.POST.get("emercontact");

#  从POST中获取银行卡信息，并赋值给user的bankcard字段    
    user.bankcard = request.POST.get("bankcard");

#  从POST中获取银行卡信息，并赋值给session的bankcard字段    
    request.session['bankcard'] = request.POST.get("bankcard");

#  从POST中获取Payslip信息，并赋值给user的payslip字段    
    user.payslip = request.POST.get("payslip");

#  从POST中获取Payslip信息，并赋值给session的payslip字段    
    request.session['payslip'] = request.POST.get("payslip");

#  使用save方法保存用户信息    
    user.save();

#  给出页面提示修改成功，并跳转到用户个人中心    
    return HttpResponse(u"<script>alert('Change successful!');window.location.href = '/loginAndRegist/userindex';</script>");

#  定义处理维修工修改个人信息的方法    
def repairmanxiugaigerenxinxiact(request):

#  获取需要修改的维修工id信息    
    id = request.POST.get("id");

#  根据传入的维修工id信息使用get方法获取维修工信息    
    repairman = models.Repairman.objects.get(id=id);

#  从POST中获取维修工id信息，并赋值给repairman的id字段    
    repairman.id = request.POST.get("id");

#  从POST中获取维修工id信息，并赋值给session的id字段    
    request.session['id'] = request.POST.get("id");

#  从POST中获取姓名信息，并赋值给repairman的name字段    
    repairman.name = request.POST.get("name");

#  从POST中获取姓名信息，并赋值给session的name字段    
    request.session['name'] = request.POST.get("name");

#  从POST中获取用户名信息，并赋值给repairman的username字段    
    repairman.username = request.POST.get("username");

#  从POST中获取用户名信息，并赋值给session的username字段    
    request.session['username'] = request.POST.get("username");

#  从POST中获取密码信息，并赋值给repairman的password字段    
    repairman.password = request.POST.get("password");

#  从POST中获取密码信息，并赋值给session的password字段    
    request.session['password'] = request.POST.get("password");

#  从POST中获取邮箱信息，并赋值给repairman的email字段    
    repairman.email = request.POST.get("email");

#  从POST中获取邮箱信息，并赋值给session的email字段    
    request.session['email'] = request.POST.get("email");

#  从POST中获取地址信息，并赋值给repairman的address字段    
    repairman.address = request.POST.get("address");

#  从POST中获取地址信息，并赋值给session的address字段    
    request.session['address'] = request.POST.get("address");

#  从POST中获取可救援类型信息，并赋值给repairman的allowtype字段    
    repairman.allowtype = request.POST.get("allowtype");

#  从POST中获取可救援类型信息，并赋值给session的allowtype字段    
    request.session['allowtype'] = request.POST.get("allowtype");

#  从POST中获取状态信息，并赋值给repairman的state字段    
    repairman.state = request.POST.get("state");

#  从POST中获取状态信息，并赋值给session的state字段    
    request.session['state'] = request.POST.get("state");

#  从POST中获取银行卡信息，并赋值给repairman的bankcard字段    
    repairman.bankcard = request.POST.get("bankcard");

#  从POST中获取银行卡信息，并赋值给session的bankcard字段    
    request.session['bankcard'] = request.POST.get("bankcard");

#  从POST中获取Payslip信息，并赋值给repairman的payslip字段    
    repairman.payslip = request.POST.get("payslip");

#  从POST中获取Payslip信息，并赋值给session的payslip字段    
    request.session['payslip'] = request.POST.get("payslip");

#  使用save方法保存维修工信息    
    repairman.save();

#  给出页面提示修改成功，并跳转到维修工个人中心    
    return HttpResponse(u"<script>alert('Change successful!');window.location.href = '/loginAndRegist/repairmanindex';</script>");




