#__author:  Administrator
#date:  2017/1/19
from django import template
from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta
from django.db.models import Sum

register = template.Library()


@register.simple_tag
def get_score(enroll_obj,customer_obj):
    study_records = enroll_obj.studyrecord_set.\
        filter(course_record__from_class_id=enroll_obj.enrolled_class.id)

    # for record in study_records:
    #     print('-->',record)
    return study_records.aggregate(Sum('score'))