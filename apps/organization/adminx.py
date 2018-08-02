# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-2 下午12:35'

import xadmin

from .models import CourseOrg, CityDict, Teacher


class CourseOrgAdmin(object):

    list_display = ['name', 'click_nums', 'fav_nums', 'students', 'city', 'add_time']
    search_fields = ['name', 'click_nums', 'fav_nums', 'students']
    list_filter = ['name', 'click_nums', 'fav_nums', 'students', 'city', 'add_time']


class CityDictAdmin(object):

    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]
    list_filter = ['name', 'desc', 'add_time']


class TeacherAdmin(object):

    list_display = ['org', 'name', 'work_years', 'work_company', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'fav_nums', 'add_time']


xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)