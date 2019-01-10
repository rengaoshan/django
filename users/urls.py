# coding:utf-8
from django.conf.urls import url
from . import views

# 创建路由列表变量
urlpatterns = [
    url('^index', views.index)
]


if __name__ == '__main__':
    pass