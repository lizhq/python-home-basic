
from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.stu_my_classes,name="stu_my_classes"),
    url(r'^studyrecords/(\d+)/$', views.studyrecords,name="studyrecords"),
    url(r'^homework_detail/(\d+)/$', views.homework_detail,name="homework_detail"),

]
