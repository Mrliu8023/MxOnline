# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-2 上午11:03'


import xadmin
from xadmin import views

from models import EmailVerifyRecord
from models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobaSettings(object):
    site_title = "佩奇后台管理系统"
    site_footer = "佩奇教育"
    menu_style = "accordion"


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

#注册主题功能
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(views.CommAdminView, GlobaSettings)