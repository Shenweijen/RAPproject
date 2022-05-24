# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import repairmanViews
urlpatterns = [

#  定义添加维修工的url地址响应方法，跳转到 repairmanView的tianjiarepairman方法     
    url(r'^tianjiarepairman/$', repairmanViews.tianjiarepairman, name='tianjiarepairman'),

#  定义处理添加维修工的url地址响应方法，跳转到 repairmanView的tianjiarepairmanact方法     
    url(r'^tianjiarepairmanact/$', repairmanViews.tianjiarepairmanact, name='tianjiarepairmanact'),

#  定义跳转修改维修工的url地址响应方法，跳转到 repairmanView的xiugairepairman方法     
    url(r'^xiugairepairman/(?P<id>[0-9]+)$', repairmanViews.xiugairepairman, name='xiugairepairman'),

#  定义处理修改维修工的url地址响应方法，跳转到 repairmanView的xiugairepairmanat方法     
    url(r'^xiugairepairmanact/$', repairmanViews.xiugairepairmanact, name='xiugairepairmanact'),

#  定义跳转管理维修工的url地址响应方法，跳转到 repairmanView的repairmanguanli方法     
    url(r'^repairmanguanli/$', repairmanViews.repairmanguanli, name='repairmanguanli'),

#  定义跳转查看维修工的url地址响应方法，跳转到 repairmanView的repairmanchakan方法     
    url(r'^repairmanchakan/$', repairmanViews.repairmanchakan, name='repairmanchakan'),

#  定义处理删除维修工的url地址响应方法，跳转到 repairmanView的shanchurepairman方法     
    url(r'^shanchurepairmanact/(?P<id>[0-9]+)$', repairmanViews.shanchurepairmanact, name='shanchurepairmanact'),

#  定义跳转搜索维修工的url地址响应方法，跳转到 repairmanView的sousuorepairman方法     
    url(r'^sousuorepairman/$', repairmanViews.sousuorepairman, name='sousuorepairman'),

#  定义维修工详情的url地址响应方法，跳转到 repairmanView的repairmanxiangqing方法     
    url(r'^repairmanxiangqing/(?P<id>[0-9]+)$', repairmanViews.repairmanxiangqing, name='repairmanxiangqing'),
]

