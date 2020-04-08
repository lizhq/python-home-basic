#__author:  Administrator
#date:  2017/1/3
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MyMiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MyMiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            # 执行当前中间的process_request
            response = self.process_request(request)
        if not response:
            # 执行下一个中间的 __call__
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            # 执行当前中间的process_response
            response = self.process_response(request, response)
        return response




class HXL(MyMiddlewareMixin):
    def process_request(self, request):
        print('hxl-->process_request')
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('hxl-->process_view')

    def process_response(self, request, response):
        print('hxl-->process_response')
        return response

    def process_exception(self, request, exception):
        print('hxl-->process_exception')

    def process_template_response(self,request,response):
        print('hxl--> process_template_response')
        return response

class LBS(MyMiddlewareMixin):

    def process_request(self, request):
        print('lbs-->process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('lbs-->process_view')

    def process_response(self, request, response):
        print('lbs-->process_response')
        return response

    def process_exception(self, request, exception):
        print('lbs-->process_exception')
        return HttpResponse('OK')

    def process_template_response(self,request,response):
        print('lbs--> process_template_response')
        return response

class GYC(MyMiddlewareMixin):
    def process_request(self, request):
        print('gyc-->process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('gyc-->process_view')

    def process_response(self, request, response):
        print('gyc-->process_response')
        return response

    def process_exception(self, request, exception):
        print('gyc-->process_exception')
        # return HttpResponse('OK')
        # print('gyc-->process_exception')
    def process_template_response(self,request,response):
        # print(request,type(request))
        # print(response,type(response))
        print('gyc--> process_template_response')
        return response
