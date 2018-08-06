# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-5 上午11:17'

from django.conf.urls import url

from .views import OrglistView

urlpatterns = (
    url(r'^orglist/$', OrglistView.as_view(), name='org_list'),
)
