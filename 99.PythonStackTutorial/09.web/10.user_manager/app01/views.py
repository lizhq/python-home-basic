from django.shortcuts import render,redirect,HttpResponse
from app01 import models
import json
# Create your views here.
# def test(request):
#     print(request.COOKIES)
#     # return HttpResponse('Ok')
#     obj = HttpResponse('Ok')
#     import datetime
#     # v = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
#     # # obj.set_cookie('k3','333333',max_age=10,expires=v,path='/')
#     # obj.set_cookie('k5','v5',max_age=10,expires=v, domain='oldboy.com')
#     # # oldboy.com   k5:v5
#     # obj.set_cookie('k6','v6')
#     obj.set_cookie('k7','v7',httponly=True)
#     return obj
#
# def xiaohu(request):
#     v = request.COOKIES.get('k7')
#     return HttpResponse(v)



"""
def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:

            rep = redirect('/index.html')
            # rep.set_cookie('username', user)
            # rep.set_cookie('account', "123123123")
            # rep.set_cookie('pwd', "asdfasdfasdfasdf")
            rep.set_signed_cookie('username', user)
            rep.set_signed_cookie('account', "123123123")
            rep.set_signed_cookie('pwd', "asdfasdfasdfasdf")
            return rep

            # return redirect('/index.html')
        else:
            message = "用户名或密码错误"
    return render(request,'login.html', {'msg': message})

def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    # username = request.COOKIES.get('username')

    username = request.get_signed_cookie('username')
    if username:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')

"""
# def js_cookie(request):
#     print(request.COOKIES)
#     obj = render(request, 'js_cookie.html')
#     obj.set_cookie('guoyongchang', 'girl')
#     return obj

from django import views
from django.utils.decorators import method_decorator
"""
def outer(func):
    def inner(request, *args, **kwargs):
        print(request.method)
        return func(request, *args, **kwargs)
    return inner



class Order(views.View):
    pass
# CBV
# @method_decorator(outer, name='dispatch')
class Login(views.View):

    # @method_decorator(outer)
    def dispatch(self, request, *args, **kwargs):
        ret = super(Login, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self,request, *args, **kwargs):
        print('GET')
        return render(request, 'login.html', {'msg': ''})

    def post(self, request, *args, **kwargs):
        print('POST')
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
            return render(request, 'login.html', {'msg': message})

"""

class Login(views.View):

    def get(self,request, *args, **kwargs):
        return render(request, 'login.html', {'msg': ''})

    def post(self, request, *args, **kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
            return render(request, 'login.html', {'msg': message})

# FBV
def login(request):
    message = ""
    v = request.session
    print(type(v))
    from django.contrib.sessions.backends.db import SessionStore
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
    obj = render(request,'login.html', {'msg': message})
    return obj

def logout(request):
    request.session.clear()
    return redirect('/login.html')


def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner

@auth
def index(request):
    current_user = request.session.get('username')
    return render(request, 'index.html',{'username': current_user})




@auth
def handle_classes(request):
    if request.method == "GET":
        # for i in range(1000):
        #     models.Classes.objects.create(caption='全栈一班'+str(i))
        # 获取所有的班级列表
        # models.Classes.objects.create(caption='全栈一班')
        # models.Classes.objects.create(caption='全栈二班')
        # models.Classes.objects.create(caption='全栈三班')

        # 当前页
        current_page = request.GET.get('p',1)
        current_page = int(current_page)

        # 所有数据的个数
        total_count = models.Classes.objects.all().count()

        from utils.page import PagerHelper
        obj = PagerHelper(total_count, current_page, '/classes.html',5)
        pager = obj.pager_str()

        cls_list = models.Classes.objects.all()[obj.db_start:obj.db_end]

        current_user = request.session.get('username')
        return render(request,
                      'classes.html',
                      {'username': current_user, 'cls_list': cls_list, 'str_pager': pager})


    elif request.method == "POST":
        # Form表单提交的处理方式
        """
        caption = request.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption=caption)
        return redirect('/classes.html')
        """
        # Ajax
        import json

        response_dict = {'status': True, 'error': None, 'data': None}

        caption = request.POST.get('caption', None)
        print(caption)
        if caption:
            obj = models.Classes.objects.create(caption=caption)
            response_dict['data'] = {'id': obj.id, 'caption': obj.caption}
        else:
            response_dict['status'] = False
            response_dict['error'] = "标题不能为空"
        return HttpResponse(json.dumps(response_dict))

@auth
def handle_add_classes(request):
    message = ""
    if request.method == "GET":
        return render(request, 'add_classes.html', {'msg': message})
    elif request.method == "POST":
        caption = request.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption=caption)
        else:
            message = "标题不能为空"
            return render(request, 'add_classes.html', {'msg': message})
        return redirect('/classes.html')
    else:
        return redirect('/index.html')

@auth
def handle_edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request, 'edit_classes.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('nid')
        caption = request.POST.get('caption')
        models.Classes.objects.filter(id=nid).update(caption=caption)
        return redirect('/classes.html')
    else:
        return redirect('/index.html')


@auth
def handle_student(request):
    if request.method == "GET":
        # for i in range(10):
        #     models.Student.objects.create(name='root' + str(i),
        #                                   email='root@live.com' + str(i),
        #                                   cls_id=i)
        result = models.Student.objects.all()
        current_user = request.session.get('username')
        return render(request, 'student.html', {'username': current_user,'result': result})
    elif request.method == "POST":
        return redirect('/index.html')
    else:
        return redirect('/index.html')


@auth
def handle_teacher(request):
    # FBV,CBV
    current_user = request.session.get('username')

    # teacher_list = models.Teacher.objects.all()
    # for obj in teacher_list:
    #     print(obj.id,obj.name,obj.cls.all())

    # teacher_list = models.Teacher.objects.filter(id__in=models.Teacher.objects.all()[0:5]).values('id','name','cls__id','cls__caption')
    teacher_list = models.Teacher.objects.filter(id__in=models.Teacher.objects.all()).values('id','name','cls__id','cls__caption')
    # select * from tb where id in (
    #     select id from tb2
    # )


    result = {}
    for t in teacher_list:
        # print(t['id'],t['name'],t['cls__id'],t['cls__caption'])
        if t['id'] in result:
            if t['cls__id']:
                result[t['id']]['cls_list'].append({'id':t['cls__id'], 'caption': t['cls__caption'] })
        else:
            if t['cls__id']:
                temp = [{'id': t['cls__id'], 'caption': t['cls__caption']},]
            else:
                temp = []
            result[t['id']] = {
                'nid': t['id'],
                'name': t['name'],
                'cls_list': temp
            }
    # class Node:
    #     def __init__(self,nid,name):
    #         self.nid = nid
    #         self.name = name
    #         self.cls_list = []

    # result = {
    #     1: {
    #         'nid': 1,
    #         'name': '仓夜空',
    #         'cls_list':[
    #             {'id': 1, 'caption': "全栈二班最牛逼"},
    #             {'id': 2, 'caption': "全栈二班"}
    #         ]
    #     },
    #     2: {
    #         'nid': 2,
    #         'name': '经夜空1',
    #         'cls_list': [
    #             {'id': 1, 'caption': "全栈二班最牛逼"},
    #             {'id': 5, 'caption': "阿萨德发生地方"}
    #         ]
    #     }
    # }

    return render(request, 'teacher.html', {'username': current_user, "teacher_list": result})

def add_teacher(request):
    if request.method == 'GET':
        cls_list = models.Classes.objects.all()
        return render(request, 'add_teacher.html', {'cls_list': cls_list})
    elif request.method == "POST":
        name = request.POST.get('name')
        cls = request.POST.getlist('cls')
        # print(name,cls)
        # 创建老师
        obj = models.Teacher.objects.create(name=name)
        # 创建老师和班级的对应关系
        obj.cls.add(*cls)


        return redirect('/teacher.html')

def edit_teacher(request,nid):
    # 获取当前老师信息
    # 获取当前老师对应的所有班级
    # - 获取所有的班级
    # - 获取当前老师未对应的所有班级
    if request.method == "GET":
        obj = models.Teacher.objects.get(id=nid)
        obj_cls_list = obj.cls.all().values_list('id')
        # [ (1,"root1"),(2,"root2"),(3,"root3"),]
        id_list = list(zip(*obj_cls_list))[0]
        # [1,2,3]
        cls_list = models.Classes.objects.all()
        # 1
        return render(request, 'edit_teacher.html', {'obj': obj, "cls_list": cls_list, "id_list": id_list})
    elif request.method == "POST":
        # nid = request.POST.get('nid')
        name = request.POST.get('name')
        cls_li = request.POST.getlist('cls')
        obj = models.Teacher.objects.get(id=nid)
        obj.name = name
        obj.save()

        obj.cls.set(cls_li)

        return redirect('/teacher.html')








#
# def test(request):
#     di = {'k1': 'v1','name': 'shahu'}
#     import json
#     return HttpResponse(json.dumps(di))
    # return render(request,'test.html',{'k1': 'v1'})
def page(request):
    return render(request, 'page.html')
@auth
def add_student(request):
    if request.method == "GET":
        cls_list = models.Classes.objects.all()[0: 20]
        return render(request, 'add_student.html', {'cls_list': cls_list})
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.create(name=name,email=email,cls_id=cls_id)
        return redirect('/student.html')
@auth
def edit_student(request):
    if request.method == "GET":
        cls_list = models.Classes.objects.all()[0: 20]
        nid = request.GET.get('nid')
        obj = models.Student.objects.get(id=nid)
        return render(request, 'edit_student.html', {'cls_list': cls_list, "obj": obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.filter(id=nid).update(name=name,email=email,cls_id=cls_id)
        return redirect('/student.html')

def menu(request):
    # for i in range(10):
    #     models.Province.objects.create(name="河北"+str(i))
    # for i in range(5):
    #     models.City.objects.create(name="廊坊" + str(i),pro_id=1)
    # return HttpResponse("OK")
    pro_list = models.Province.objects.all()
    return render(request, 'menus.html', {"pro_list": pro_list})

def fetch_city(request):
    # 根据用户传入的省份ID，获取与其相关的所有市ID
    # ret = {'status': True, 'error': None, 'data': None}

    province_id = request.GET.get('province_id')
    # result = models.City.objects.filter(pro_id=province_id)
    # # QuerySet内部放置对象
    # from django.core import serializers
    # data = serializers.serialize("json", result)

    result = models.City.objects.filter(pro_id=province_id).values('id','name')
    # QuerySet内部放置对象
    result = list(result)
    import json
    data = json.dumps(result)

    # result = models.City.objects.filter(pro_id=province_id).values_list('id','name')
    # # QuerySet内部放置对象
    # print(result)
    # result = list(result)
    # import json
    # data = json.dumps(result)

    return HttpResponse(data)

def fetch_xian(request):
    # for i in range(10):
    #     models.Xian.objects.create(name='县'+ str(i), cy_id=1)
    city_id = request.GET.get('city_id')
    xian_list = models.Xian.objects.filter(cy_id=city_id).values('id','name')
    xian_list = list(xian_list)
    return HttpResponse(json.dumps(xian_list))

def test(request):
    # pro_list = models.Province.objects.all()
    # print(pro_list)
    # city_list = models.City.objects.all()
    # print(city_list)
    # 正向查找（具有外键字段）
    # filter(故意写错)
    # v = models.City.objects.all()
    # print(v)
    # 反向
    # v = models.Province.objects.values('id','name','city__name')
    # print(v)
    # pro_list = models.Province.objects.all()
    # for item in pro_list:
    #     print(item.id,item.name,item.city_set.filter(id__lt=3))

    # models.Book.objects.create(name='书名')
    # models.Author.objects.create(name='人名')
    # 正向查找
    # obj,人，金鑫
    # obj = models.Author.objects.get(id=1)
    #
    # # 金鑫所有的著作全部获取到
    # obj.m.all()

    # 反向查找
    # 金品买
    # obj = models.Book.objects.get(id=1)
    # # 金鑫，吴超
    # obj.author_set.all()
    # 10
    # author_list = models.Author.objects.all()
    # for author in author_list:
    #     print(author.name,author.m.all())

    # author_list = models.Author.objects.values('id','name','m', "m__name")
    # for item in author_list:
    #     print(item['id'],item['name'],'书籍ID:',item['m'],item['m__name'])

    # 添加

    # obj = models.Author.objects.get(id=1)
    # 第三张表中增加一个对应关系
    # 增加
    # obj.m.add(5)
    # obj.m.add(5,6)
    # obj.m.add(*[4,5])
    # 删除
    # obj.m.remove(5)
    # obj.m.remove(5,6)
    # obj.m.remove(*[5,6])
    # 清空
    # obj.m.clear()
    # 更新
    # obj.m.set([1,2,3])

    # 反向操作
    # obj = models.Book.objects.get(id=1)
    # obj.author_set.add(1)
    # obj.author_set.add(1,2,3,4)
    # ...


    return HttpResponse("OK")

