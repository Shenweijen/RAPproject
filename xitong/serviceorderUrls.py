# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import serviceorderViews
urlpatterns = [

#  定义添加会员服务的url地址响应方法，跳转到 serviceorderView的tianjiaserviceorder方法     
    url(r'^tianjiaserviceorder/$', serviceorderViews.tianjiaserviceorder, name='tianjiaserviceorder'),

#  定义处理添加会员服务的url地址响应方法，跳转到 serviceorderView的tianjiaserviceorderact方法     
    url(r'^tianjiaserviceorderact/$', serviceorderViews.tianjiaserviceorderact, name='tianjiaserviceorderact'),

#  定义跳转修改会员服务的url地址响应方法，跳转到 serviceorderView的xiugaiserviceorder方法     
    url(r'^xiugaiserviceorder/(?P<id>[0-9]+)$', serviceorderViews.xiugaiserviceorder, name='xiugaiserviceorder'),

#  定义处理修改会员服务的url地址响应方法，跳转到 serviceorderView的xiugaiserviceorderat方法     
    url(r'^xiugaiserviceorderact/$', serviceorderViews.xiugaiserviceorderact, name='xiugaiserviceorderact'),

#  定义跳转管理会员服务的url地址响应方法，跳转到 serviceorderView的serviceorderguanli方法     
    url(r'^serviceorderguanli/$', serviceorderViews.serviceorderguanli, name='serviceorderguanli'),

#  定义跳转查看会员服务的url地址响应方法，跳转到 serviceorderView的serviceorderchakan方法     
    url(r'^serviceorderchakan/$', serviceorderViews.serviceorderchakan, name='serviceorderchakan'),

#  定义处理删除会员服务的url地址响应方法，跳转到 serviceorderView的shanchuserviceorder方法     
    url(r'^shanchuserviceorderact/(?P<id>[0-9]+)$', serviceorderViews.shanchuserviceorderact, name='shanchuserviceorderact'),

#  定义跳转搜索会员服务的url地址响应方法，跳转到 serviceorderView的sousuoserviceorder方法     
    url(r'^sousuoserviceorder/$', serviceorderViews.sousuoserviceorder, name='sousuoserviceorder'),

#  定义会员服务详情的url地址响应方法，跳转到 serviceorderView的serviceorderxiangqing方法     
    url(r'^serviceorderxiangqing/(?P<id>[0-9]+)$', serviceorderViews.serviceorderxiangqing, name='serviceorderxiangqing'),

#  定义添加会员服务方法，响应页面请求，跳转到serviceorderViews的usertianjiaserviceorder方法  
    url(r'^usertianjiaserviceorder/$', serviceorderViews.usertianjiaserviceorder, name='usertianjiaserviceorder'),

#  定义处理添加会员服务方法，响应页面请求，跳转到serviceorderViews的usertianjiaserviceorderact方法  
    url(r'^usertianjiaserviceorderact/$', serviceorderViews.usertianjiaserviceorderact, name='usertianjiaserviceorderact'),

#  定义跳转修改会员服务方法，响应页面请求，跳转到serviceorderViews的userxiugaiserviceorder方法  
    url(r'^userxiugaiserviceorder/(?P<id>[0-9]+)$', serviceorderViews.userxiugaiserviceorder, name='userxiugaiserviceorder'),

#  定义处理修改会员服务方法，响应页面请求，跳转到serviceorderViews的userxiugaiserviceorderact方法  
    url(r'^userxiugaiserviceorderact/$', serviceorderViews.userxiugaiserviceorderact, name='userxiugaiserviceorderact'),

#  定义跳转会员服务管理方法，响应页面请求，跳转到serviceorderViews的userserviceorderguanli方法  
    url(r'^userserviceorderguanli/$', serviceorderViews.userserviceorderguanli, name='userserviceorderguanli'),

#  定义处理删除会员服务方法，响应页面请求，跳转到serviceorderViews的usershanchuserviceorder方法  
    url(r'^usershanchuserviceorderact/(?P<id>[0-9]+)$', serviceorderViews.usershanchuserviceorderact, name='usershanchuserviceorderact'),
]

