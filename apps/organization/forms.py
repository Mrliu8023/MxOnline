# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-21 上午10:33'

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']