# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import rescueorderViews
urlpatterns = [

#  定义添加订单的url地址响应方法，跳转到 rescueorderView的tianjiarescueorder方法     
    url(r'^tianjiarescueorder/$', rescueorderViews.tianjiarescueorder, name='tianjiarescueorder'),

#  定义处理添加订单的url地址响应方法，跳转到 rescueorderView的tianjiarescueorderact方法     
    url(r'^tianjiarescueorderact/$', rescueorderViews.tianjiarescueorderact, name='tianjiarescueorderact'),

#  定义跳转修改订单的url地址响应方法，跳转到 rescueorderView的xiugairescueorder方法     
    url(r'^xiugairescueorder/(?P<id>[0-9]+)$', rescueorderViews.xiugairescueorder, name='xiugairescueorder'),

#  定义处理修改订单的url地址响应方法，跳转到 rescueorderView的xiugairescueorderat方法     
    url(r'^xiugairescueorderact/$', rescueorderViews.xiugairescueorderact, name='xiugairescueorderact'),

#  定义跳转管理订单的url地址响应方法，跳转到 rescueorderView的rescueorderguanli方法     
    url(r'^rescueorderguanli/$', rescueorderViews.rescueorderguanli, name='rescueorderguanli'),

#  定义跳转查看订单的url地址响应方法，跳转到 rescueorderView的rescueorderchakan方法     
    url(r'^rescueorderchakan/$', rescueorderViews.rescueorderchakan, name='rescueorderchakan'),

    url(r'^repairmanrescueorderchakan/$', rescueorderViews.repairmanrescueorderchakan, name='repairmanrescueorderchakan'),

#  定义处理删除订单的url地址响应方法，跳转到 rescueorderView的shanchurescueorder方法     
    url(r'^shanchurescueorderact/(?P<id>[0-9]+)$', rescueorderViews.shanchurescueorderact, name='shanchurescueorderact'),

    url(r'^wancheng/(?P<id>[0-9]+)$', rescueorderViews.wancheng, name='wancheng'),

    url(r'^tongguo/(?P<id>[0-9]+)$', rescueorderViews.tongguo, name='tongguo'),

    url(r'^jiedan/(?P<id>[0-9]+)$', rescueorderViews.jiedan, name='jiedan'),

#  定义跳转搜索订单的url地址响应方法，跳转到 rescueorderView的sousuorescueorder方法     
    url(r'^sousuorescueorder/$', rescueorderViews.sousuorescueorder, name='sousuorescueorder'),

#  定义订单详情的url地址响应方法，跳转到 rescueorderView的rescueorderxiangqing方法     
    url(r'^rescueorderxiangqing/(?P<id>[0-9]+)$', rescueorderViews.rescueorderxiangqing, name='rescueorderxiangqing'),

#  定义添加订单方法，响应页面请求，跳转到rescueorderViews的usertianjiarescueorder方法  
    url(r'^usertianjiarescueorder/$', rescueorderViews.usertianjiarescueorder, name='usertianjiarescueorder'),

#  定义处理添加订单方法，响应页面请求，跳转到rescueorderViews的usertianjiarescueorderact方法  
    url(r'^usertianjiarescueorderact/$', rescueorderViews.usertianjiarescueorderact, name='usertianjiarescueorderact'),

#  定义跳转修改订单方法，响应页面请求，跳转到rescueorderViews的userxiugairescueorder方法  
    url(r'^userxiugairescueorder/(?P<id>[0-9]+)$', rescueorderViews.userxiugairescueorder, name='userxiugairescueorder'),

#  定义处理修改订单方法，响应页面请求，跳转到rescueorderViews的userxiugairescueorderact方法  
    url(r'^userxiugairescueorderact/$', rescueorderViews.userxiugairescueorderact, name='userxiugairescueorderact'),

#  定义跳转订单管理方法，响应页面请求，跳转到rescueorderViews的userrescueorderguanli方法  
    url(r'^userrescueorderguanli/$', rescueorderViews.userrescueorderguanli, name='userrescueorderguanli'),

#  定义处理删除订单方法，响应页面请求，跳转到rescueorderViews的usershanchurescueorder方法  
    url(r'^usershanchurescueorderact/(?P<id>[0-9]+)$', rescueorderViews.usershanchurescueorderact, name='usershanchurescueorderact'),
]

