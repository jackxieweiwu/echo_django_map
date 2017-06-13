# -*- coding:utf8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
import echo.views

urlpatterns = [
# the sitemap

    url(r'^admin/', admin.site.urls),
    url(r'^index/', echo.views.index,name= 'index'),

    #用户登陆列表
    #用户登陆
    url(r'login/', echo.views.login, name='login'),
    #用户注册
    #url(r'register/', echo.views.register, name='register'),
    #用户退出
    url(r'logout/', echo.views.logout, name='logout'),
    #密码修改
    url(r'password_change/', echo.views.password_change, name='password_change'),

    #基础资料的显示
    #内容显示,并通过定义name，来进行反向解析
    url(r'^lists/(?P<table>\w+)/$', echo.views.lists, name='lists'),
    #增加内容
    url(r'^add/(?P<table>\w+)/$', echo.views.add, name='add'),
    #修改数据,?P<pk>\d+代表穿过来的id值，且id值一定为数字
    url(r'^edit/(?P<table>\w+)/(?P<pk>\d+)/$', echo.views.edit, name='edit'),
    #删除数据
    url(r'^delete/(?P<table>\w+)/(?P<pk>\d+)/$', echo.views.delete, name='delete'),


    #任务列表
    url(r'^task_list/', echo.views.task_list, name='task_list'),
    url(r'^task_add/', echo.views.task_add, name='task_add'),
    url(r'^task_edit/(?P<pk>\d+)/$', echo.views.task_edit, name='task_edit'),
    url(r'^task_delete/(?P<pk>\d+)/$', echo.views.task_delete, name='task_delete'),
    url(r'^task_finish/(?P<pk>\d+)/$',echo.views.task_finish, name='task_finish'),


    #实施步骤
    url(r'^process_edit/(?P<pk>\d+)/$', echo.views.process_edit, name='process_edit'),
    url(r'^process_delete/(?P<pk>\d+)/$',echo.views.process_delete, name='process_delete'),

    #上传附件
    url(r'^upload_file/(?P<pk>\d+)/$', echo.views.upload_file, name='upload_file'),



]

#在测试环境中，将
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)