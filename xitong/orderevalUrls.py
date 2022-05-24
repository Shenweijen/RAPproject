# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import orderevalViews
urlpatterns = [

#  定义添加订单评价的url地址响应方法，跳转到 orderevalView的tianjiaordereval方法     
    url(r'^tianjiaordereval/$', orderevalViews.tianjiaordereval, name='tianjiaordereval'),

#  定义处理添加订单评价的url地址响应方法，跳转到 orderevalView的tianjiaorderevalact方法     
    url(r'^tianjiaorderevalact/$', orderevalViews.tianjiaorderevalact, name='tianjiaorderevalact'),

#  定义跳转修改订单评价的url地址响应方法，跳转到 orderevalView的xiugaiordereval方法     
    url(r'^xiugaiordereval/(?P<id>[0-9]+)$', orderevalViews.xiugaiordereval, name='xiugaiordereval'),

#  定义处理修改订单评价的url地址响应方法，跳转到 orderevalView的xiugaiorderevalat方法     
    url(r'^xiugaiorderevalact/$', orderevalViews.xiugaiorderevalact, name='xiugaiorderevalact'),

#  定义跳转管理订单评价的url地址响应方法，跳转到 orderevalView的orderevalguanli方法     
    url(r'^orderevalguanli/$', orderevalViews.orderevalguanli, name='orderevalguanli'),

#  定义跳转查看订单评价的url地址响应方法，跳转到 orderevalView的orderevalchakan方法     
    url(r'^orderevalchakan/$', orderevalViews.orderevalchakan, name='orderevalchakan'),

#  定义处理删除订单评价的url地址响应方法，跳转到 orderevalView的shanchuordereval方法     
    url(r'^shanchuorderevalact/(?P<id>[0-9]+)$', orderevalViews.shanchuorderevalact, name='shanchuorderevalact'),

#  定义跳转搜索订单评价的url地址响应方法，跳转到 orderevalView的sousuoordereval方法     
    url(r'^sousuoordereval/$', orderevalViews.sousuoordereval, name='sousuoordereval'),

#  定义订单评价详情的url地址响应方法，跳转到 orderevalView的orderevalxiangqing方法     
    url(r'^orderevalxiangqing/(?P<id>[0-9]+)$', orderevalViews.orderevalxiangqing, name='orderevalxiangqing'),

#  定义添加订单评价方法，响应页面请求，跳转到orderevalViews的usertianjiaordereval方法  
    url(r'^usertianjiaordereval/$', orderevalViews.usertianjiaordereval, name='usertianjiaordereval'),

#  定义处理添加订单评价方法，响应页面请求，跳转到orderevalViews的usertianjiaorderevalact方法  
    url(r'^usertianjiaorderevalact/$', orderevalViews.usertianjiaorderevalact, name='usertianjiaorderevalact'),

#  定义跳转修改订单评价方法，响应页面请求，跳转到orderevalViews的userxiugaiordereval方法  
    url(r'^userxiugaiordereval/(?P<id>[0-9]+)$', orderevalViews.userxiugaiordereval, name='userxiugaiordereval'),

#  定义处理修改订单评价方法，响应页面请求，跳转到orderevalViews的userxiugaiorderevalact方法  
    url(r'^userxiugaiorderevalact/$', orderevalViews.userxiugaiorderevalact, name='userxiugaiorderevalact'),

#  定义跳转订单评价管理方法，响应页面请求，跳转到orderevalViews的userorderevalguanli方法  
    url(r'^userorderevalguanli/$', orderevalViews.userorderevalguanli, name='userorderevalguanli'),

#  定义处理删除订单评价方法，响应页面请求，跳转到orderevalViews的usershanchuordereval方法  
    url(r'^usershanchuorderevalact/(?P<id>[0-9]+)$', orderevalViews.usershanchuorderevalact, name='usershanchuorderevalact'),
]

