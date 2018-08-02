# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-2 上午11:03'


import xadmin

from models import EmailVerifyRecord
from models import Banner


class EmailVerifyRecordAdmin(object):

    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):

    list_display = ['image', 'title', 'url', 'index','add_time']
    search_fields = ['image', 'title', 'url', 'index']
    list_filter = ['image', 'title', 'url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)