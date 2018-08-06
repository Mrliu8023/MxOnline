# _*_ coding:utf-8 _*_

from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from models import CityDict, CourseOrg


class OrglistView(View):
    def get(self, request):
        all_citys = CityDict.objects.all()
        #citys去重
        # citys = []
        # for i in all_citys:
        #     if i.name not in citys:
        #         citys.append(i.name)

        course_orgs = CourseOrg.objects.all()
        org_nums = course_orgs.count()
        context = {
            "citys": all_citys,
            "course_orgs": course_orgs,
            "org_nums": org_nums,
        }
        return render(request, 'organization/org-list.html', context)
