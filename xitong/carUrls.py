# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import carViews
urlpatterns = [

#  定义添加车辆的url地址响应方法，跳转到 carView的tianjiacar方法     
    url(r'^tianjiacar/$', carViews.tianjiacar, name='tianjiacar'),

#  定义处理添加车辆的url地址响应方法，跳转到 carView的tianjiacaract方法     
    url(r'^tianjiacaract/$', carViews.tianjiacaract, name='tianjiacaract'),

#  定义跳转修改车辆的url地址响应方法，跳转到 carView的xiugaicar方法     
    url(r'^xiugaicar/(?P<id>[0-9]+)$', carViews.xiugaicar, name='xiugaicar'),

#  定义处理修改车辆的url地址响应方法，跳转到 carView的xiugaicarat方法     
    url(r'^xiugaicaract/$', carViews.xiugaicaract, name='xiugaicaract'),

#  定义跳转管理车辆的url地址响应方法，跳转到 carView的carguanli方法     
    url(r'^carguanli/$', carViews.carguanli, name='carguanli'),

#  定义跳转查看车辆的url地址响应方法，跳转到 carView的carchakan方法     
    url(r'^carchakan/$', carViews.carchakan, name='carchakan'),

#  定义处理删除车辆的url地址响应方法，跳转到 carView的shanchucar方法     
    url(r'^shanchucaract/(?P<id>[0-9]+)$', carViews.shanchucaract, name='shanchucaract'),

#  定义跳转搜索车辆的url地址响应方法，跳转到 carView的sousuocar方法     
    url(r'^sousuocar/$', carViews.sousuocar, name='sousuocar'),

#  定义车辆详情的url地址响应方法，跳转到 carView的carxiangqing方法     
    url(r'^carxiangqing/(?P<id>[0-9]+)$', carViews.carxiangqing, name='carxiangqing'),

#  定义添加车辆方法，响应页面请求，跳转到carViews的usertianjiacar方法  
    url(r'^usertianjiacar/$', carViews.usertianjiacar, name='usertianjiacar'),

#  定义处理添加车辆方法，响应页面请求，跳转到carViews的usertianjiacaract方法  
    url(r'^usertianjiacaract/$', carViews.usertianjiacaract, name='usertianjiacaract'),

#  定义跳转修改车辆方法，响应页面请求，跳转到carViews的userxiugaicar方法  
    url(r'^userxiugaicar/(?P<id>[0-9]+)$', carViews.userxiugaicar, name='userxiugaicar'),

#  定义处理修改车辆方法，响应页面请求，跳转到carViews的userxiugaicaract方法  
    url(r'^userxiugaicaract/$', carViews.userxiugaicaract, name='userxiugaicaract'),

#  定义跳转车辆管理方法，响应页面请求，跳转到carViews的usercarguanli方法  
    url(r'^usercarguanli/$', carViews.usercarguanli, name='usercarguanli'),

#  定义处理删除车辆方法，响应页面请求，跳转到carViews的usershanchucar方法  
    url(r'^usershanchucaract/(?P<id>[0-9]+)$', carViews.usershanchucaract, name='usershanchucaract'),
]

