# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import scheduleViews
urlpatterns = [

#  定义添加日程的url地址响应方法，跳转到 scheduleView的tianjiaschedule方法     
    url(r'^tianjiaschedule/$', scheduleViews.tianjiaschedule, name='tianjiaschedule'),

#  定义处理添加日程的url地址响应方法，跳转到 scheduleView的tianjiascheduleact方法     
    url(r'^tianjiascheduleact/$', scheduleViews.tianjiascheduleact, name='tianjiascheduleact'),

#  定义跳转修改日程的url地址响应方法，跳转到 scheduleView的xiugaischedule方法     
    url(r'^xiugaischedule/(?P<id>[0-9]+)$', scheduleViews.xiugaischedule, name='xiugaischedule'),

#  定义处理修改日程的url地址响应方法，跳转到 scheduleView的xiugaischeduleat方法     
    url(r'^xiugaischeduleact/$', scheduleViews.xiugaischeduleact, name='xiugaischeduleact'),

#  定义跳转管理日程的url地址响应方法，跳转到 scheduleView的scheduleguanli方法     
    url(r'^scheduleguanli/$', scheduleViews.scheduleguanli, name='scheduleguanli'),

#  定义跳转查看日程的url地址响应方法，跳转到 scheduleView的schedulechakan方法     
    url(r'^schedulechakan/$', scheduleViews.schedulechakan, name='schedulechakan'),

#  定义处理删除日程的url地址响应方法，跳转到 scheduleView的shanchuschedule方法     
    url(r'^shanchuscheduleact/(?P<id>[0-9]+)$', scheduleViews.shanchuscheduleact, name='shanchuscheduleact'),

#  定义跳转搜索日程的url地址响应方法，跳转到 scheduleView的sousuoschedule方法     
    url(r'^sousuoschedule/$', scheduleViews.sousuoschedule, name='sousuoschedule'),

#  定义日程详情的url地址响应方法，跳转到 scheduleView的schedulexiangqing方法     
    url(r'^schedulexiangqing/(?P<id>[0-9]+)$', scheduleViews.schedulexiangqing, name='schedulexiangqing'),

#  定义添加日程方法，响应页面请求，跳转到scheduleViews的repairmantianjiaschedule方法  
    url(r'^repairmantianjiaschedule/$', scheduleViews.repairmantianjiaschedule, name='repairmantianjiaschedule'),

#  定义处理添加日程方法，响应页面请求，跳转到scheduleViews的repairmantianjiascheduleact方法  
    url(r'^repairmantianjiascheduleact/$', scheduleViews.repairmantianjiascheduleact, name='repairmantianjiascheduleact'),

#  定义跳转修改日程方法，响应页面请求，跳转到scheduleViews的repairmanxiugaischedule方法  
    url(r'^repairmanxiugaischedule/(?P<id>[0-9]+)$', scheduleViews.repairmanxiugaischedule, name='repairmanxiugaischedule'),

#  定义处理修改日程方法，响应页面请求，跳转到scheduleViews的repairmanxiugaischeduleact方法  
    url(r'^repairmanxiugaischeduleact/$', scheduleViews.repairmanxiugaischeduleact, name='repairmanxiugaischeduleact'),

#  定义跳转日程管理方法，响应页面请求，跳转到scheduleViews的repairmanscheduleguanli方法  
    url(r'^repairmanscheduleguanli/$', scheduleViews.repairmanscheduleguanli, name='repairmanscheduleguanli'),

#  定义处理删除日程方法，响应页面请求，跳转到scheduleViews的repairmanshanchuschedule方法  
    url(r'^repairmanshanchuscheduleact/(?P<id>[0-9]+)$', scheduleViews.repairmanshanchuscheduleact, name='repairmanshanchuscheduleact'),
]

