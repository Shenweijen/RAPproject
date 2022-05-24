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


#    定义添加日程的方法，响应页面请求
def tianjiaschedule(request):

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();



#  返回添加日程页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/tianjiaschedule.html',{'repairmanall':repairmanall,});


#  处理添加日程方法   
def tianjiascheduleact(request):

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

#  从页面post数据中获取内容   
    contentstr = request.POST.get("content");
    content = "";
    if(contentstr is not None):
        content = contentstr;

#  从页面post数据中获取时间   
    plandatestr = request.POST.get("plandate");
    plandate = "";
    if(plandatestr is not None):
        plandate = plandatestr;

#  从页面post数据中获取状态   
    statestr = request.POST.get("state");
    state = "";
    if(statestr is not None):
        state = statestr;

#  将日程的属性赋值给日程，生成日程对象   
    schedule = models.Schedule(repairman=repairman,repairmanid=repairmanid,content=content,plandate=plandate,state=state,);

#  调用save方法保存日程信息   
    schedule.save();



#  返回页面提示信息,添加日程成功,并跳转到日程管理页面   
    return HttpResponse(u"<script>alert('添加日程成功');window.location.href = '/schedule/scheduleguanli';</script>");


#  定义表名管理方法，响应页面scheduleguanli请求   
def scheduleguanli(request):

#  通过all方法查询所有的日程信息   
    scheduleall = models.Schedule.objects.all()



#  跳转到日程管理页面，并附带所有日程信息   
    return  render(request,'xitong/scheduleguanli.html',{'scheduleall':scheduleall});


#  定义表名查看方法，响应页面schedulechakan请求   
def schedulechakan(request):

#  通过all方法查询所有的日程信息   
    scheduleall = models.Schedule.objects.all()



#  跳转到日程查看页面，并附带所有日程信息   
    return  render(request,'xitong/schedulechakan.html',{'scheduleall':scheduleall});


#  定义修改日程方法，通过id查询对应的日程信息，返回页面展示  
def xiugaischedule(request,id):

#  使用get方法，通过id查询对应的日程信息  
    schedule = models.Schedule.objects.get(id=id);

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();


#  跳转到修改日程页面，并附带当前日程信息   
    return render(request, 'xitong/xiugaischedule.html', {'schedule': schedule,'repairmanall':repairmanall,});


#  定义处理修改日程方法   
def xiugaischeduleact(request):

#  使用request获取post中的日程id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的日程id获取对应的日程信息   
    schedule = models.Schedule.objects.get(id=id);

#  从页面post数据中获取维修工并赋值给schedule的repairman字段   
    repairmanstr = request.POST.get("repairman");
    if(repairmanstr is not None):
        schedule.repairman = repairmanstr;

#  从页面post数据中获取维修工id并赋值给schedule的repairmanid字段   
    repairmanidstr = request.POST.get("repairmanid");
    if(repairmanidstr is not None):
        schedule.repairmanid = repairmanidstr;

#  从页面post数据中获取内容并赋值给schedule的content字段   
    contentstr = request.POST.get("content");
    if(contentstr is not None):
        schedule.content = contentstr;

#  从页面post数据中获取时间并赋值给schedule的plandate字段   
    plandatestr = request.POST.get("plandate");
    if(plandatestr is not None):
        schedule.plandate = plandatestr;

#  从页面post数据中获取状态并赋值给schedule的state字段   
    statestr = request.POST.get("state");
    if(statestr is not None):
        schedule.state = statestr;

#  调用save方法保存日程信息   
    schedule.save();



#  返回页面提示信息,修改日程成功,并跳转到日程管理页面   
    return HttpResponse(u"<script>alert('修改日程成功');window.location.href = '/schedule/scheduleguanli';</script>");


#  定义删除日程方法   
def shanchuscheduleact(request,id):

#  调用django的delete方法，根据id删除日程信息   
    models.Schedule.objects.filter(id=id).delete();



#  返回页面提示信息,删除日程成功,并跳转到日程管理页面   
    return HttpResponse(u"<script>alert('删除日程成功');window.location.href = '/schedule/scheduleguanli';</script>");


#  定义搜索日程方法，响应页面搜索请求   
def sousuoschedule(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的日程信息   
    scheduleall = models.Schedule.objects.filter(repairman__icontains=search);

#  跳转到搜索日程页面，并附带查询的日程信息   
    return render(request, 'xitong/sousuoschedule.html', {"scheduleall": scheduleall});


#  处理日程详情   
def schedulexiangqing(request,id):

#  根据页面传入id获取日程信息   
    schedule = models.Schedule.objects.get(id=id);



#  跳转到日程详情页面,并日程信息传递到页面中   
    return render(request, 'xitong/schedulexiangqing.html', {"schedule": schedule});


#  定义跳转repairman添加日程页面的方法  
def repairmantianjiaschedule(request):

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();



#  返回repairman添加日程页面      
    return  render(request,'xitong/repairmantianjiaschedule.html',{'repairmanall':repairmanall,});


#  处理添加日程方法   
def repairmantianjiascheduleact(request):

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

#  从页面post数据中获取内容   
    contentstr = request.POST.get("content");
    content = "";
    if(contentstr is not None):
        content = contentstr;

#  从页面post数据中获取时间   
    plandatestr = request.POST.get("plandate");
    plandate = "";
    if(plandatestr is not None):
        plandate = plandatestr;

#  从页面post数据中获取状态   
    statestr = request.POST.get("state");
    state = "";
    if(statestr is not None):
        state = statestr;

#  将日程的属性赋值给日程，生成日程对象   
    schedule = models.Schedule(repairman=repairman,repairmanid=repairmanid,content=content,plandate=plandate,state=state,);

#  调用save方法保存日程信息   
    schedule.save();



#  返回页面提示信息,添加日程成功,并跳转到日程管理页面   
    return HttpResponse(u"<script>alert('添加日程成功');window.location.href = '/schedule/repairmanscheduleguanli';</script>");




#  跳转repairman日程管理页面      
def repairmanscheduleguanli(request):

#  查询出repairmanid等于当前用户id的所有日程信息      
    scheduleall = models.Schedule.objects.filter(repairmanid=request.session["id"])



#  返回日程管理页面，并携带scheduleall的数据信息      
    return  render(request,'xitong/repairmanscheduleguanli.html',{'scheduleall':scheduleall});


#  定义跳转repairman修改日程页面      
def repairmanxiugaischedule(request,id):

#  根据页面传入的日程id信息，查询出对应的日程信息      
    schedule = models.Schedule.objects.get(id=id);

#  获取页面数据repairman,使用DJANGO all方法查询所有数据   
    repairmanall = models.Repairman.objects.all();


#  跳转到修改日程页面，并携带查询出的日程信息      
    return render(request, 'xitong/repairmanxiugaischedule.html', {'schedule': schedule,'repairmanall':repairmanall,});


#  定义处理修改日程方法   
def repairmanxiugaischeduleact(request):

#  使用request获取post中的日程id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的日程id获取对应的日程信息   
    schedule = models.Schedule.objects.get(id=id);

#  从页面post数据中获取维修工并赋值给schedule的repairman字段   
    repairmanstr = request.POST.get("repairman");
    if(repairmanstr is not None):
        schedule.repairman = repairmanstr;

#  从页面post数据中获取维修工id并赋值给schedule的repairmanid字段   
    repairmanidstr = request.POST.get("repairmanid");
    if(repairmanidstr is not None):
        schedule.repairmanid = repairmanidstr;

#  从页面post数据中获取内容并赋值给schedule的content字段   
    contentstr = request.POST.get("content");
    if(contentstr is not None):
        schedule.content = contentstr;

#  从页面post数据中获取时间并赋值给schedule的plandate字段   
    plandatestr = request.POST.get("plandate");
    if(plandatestr is not None):
        schedule.plandate = plandatestr;

#  从页面post数据中获取状态并赋值给schedule的state字段   
    statestr = request.POST.get("state");
    if(statestr is not None):
        schedule.state = statestr;

#  调用save方法保存日程信息   
    schedule.save();



#  返回页面提示信息,修改日程成功,并跳转到日程管理页面   
    return HttpResponse(u"<script>alert('修改日程成功');window.location.href = '/schedule/repairmanscheduleguanli';</script>");




#  定义repairman删除日程信息     
def repairmanshanchuscheduleact(request,id):

#  根据页面传入的日程id信息，删除出对应的日程信息      
    models.Schedule.objects.filter(id=id).delete();



#  在页面给出提示信息，删除日程成功，并跳转到日程管理页面      
    return HttpResponse(u"<script>alert('删除日程成功');window.location.href = '/schedule/repairmanscheduleguanli';</script>");





