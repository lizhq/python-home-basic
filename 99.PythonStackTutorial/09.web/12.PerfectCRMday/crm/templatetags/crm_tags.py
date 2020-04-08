#__author:  Administrator
#date:  2017/1/18
from django import template
from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta
register = template.Library()

@register.simple_tag
def render_enroll_contract( enroll_obj):

    return enroll_obj.enrolled_class.contract.template.\
        format(course_name=enroll_obj.enrolled_class, stu_name=enroll_obj.customer.qq)