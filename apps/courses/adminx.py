# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-2 上午11:38'

import xadmin

from .models import Course, Lesson, Video, ConrseResourse


class CourseAdmin(object):

    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','click_nums']
    list_filter = ['name', 'detail', 'degree','learn_times','students','fav_nums','click_nums','add_time']


class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course__name', 'add_time']


class VideoAdmin(object):

    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson__name', 'add_time']


class CourseResourceAdmin(object):

    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course', 'download', 'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(ConrseResourse,CourseResourceAdmin)


