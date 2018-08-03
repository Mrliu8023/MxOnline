# _*_ coding:utf-8 _*_
__author__ = "peiqi"
__date__ = '18-8-3 上午9:47'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)  #username应和表单中的名称一致，required表示是否可为空，true表不为空
    password = forms.CharField(required=True, min_length=8)