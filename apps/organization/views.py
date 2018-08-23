# _*_ coding:utf-8 _*_
import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


from models import CityDict, CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from forms import UserAskForm


class OrglistView(View):
    def get(self, request):
        # 获取所有城市,机构
        all_citys = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()
        #机构排名
        hot_orgs = CourseOrg.objects.order_by("-click_nums")[:4]
        # 根据城市筛选机构
        id = request.GET.get("city", "")
        if id:
            all_orgs = all_orgs.filter(city_id=id)

        catgory = request.GET.get("ct", "")
        #根据机构类型筛选
        if catgory:
            all_orgs = all_orgs.filter(catgory=catgory)
        #根据学习人数排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")


        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        org_nums = all_orgs.count()
        context = {
            "citys": all_citys,
            "course_orgs": orgs,
            "org_nums": org_nums,
            "city_id": id,
            "catgory": catgory,
            "sort": sort,
            "hot_orgs": hot_orgs,
        }
        return render(request, 'organization/org-list.html', context)


class UserAskView(View):
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask = userask_form.save(commit=True)
            ctx = {"status":"success"}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
        else:
            ctx = {"status": "fail", "msg": u"添加错误"}
            return HttpResponse(json.dumps(ctx), content_type='application/json;charset=utf-8')