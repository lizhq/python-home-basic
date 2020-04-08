from django.shortcuts import render,HttpResponse

# Create your views here.

class Foo:
    def __init__(self, request,html):
        self.req = request
        self.html = html

    def render(self):
        return render(self.req,self.html)


def test(request,nid):
    print('views')
    # int('asdf')
    # return HttpResponse('TEST')
    # return render(request, 'test.html')
    # --> HttpResponse
    return Foo(request,'test.html')