#__author:  Administrator
#date:  2017/1/19

#url type : 0 = related , 1 absolute

perm_dic = {
     'crm.can_access_my_course': {
         'url_type':0,
         'url': 'stu_my_classes', #url name
         'method': 'GET',
         'args': []
     },
    'crm.can_access_customer_list':{
        'url_type':1,
        'url': '/king_admin/crm/customer/',  # url name
        'method': 'GET',
        'args': []
    },
    '__crm.can_access_customer_detail':{
        'url_type':0,
        'url': 'table_obj_change',  # url name
        'method': 'GET',
        'args': []
    },
    'crm.can_access_studyrecords': {
        'url_type': 0,
        'url': 'studyrecords',  # url name
        'method': 'GET',
        'args': []
    },
    'crm.can_access_homework_detail': {
        'url_type': 0,
        'url': 'homework_detail',  # url name
        'method': 'GET',
        'args': []
    },
    'crm.can_upload_homework': {
        'url_type': 0,
        'url': 'homework_detail',  # url name
        'method': 'POST',
        'args': []
    },
    'crm.access_kingadmin_table_obj_detail': {
        'url_type': 0,
        'url': 'table_obj_change',  # url name
        'method': 'GET',
        'args': []
    },
    'crm.change_kingadmin_table_obj_detail': {
        'url_type': 0,
        'url': 'table_obj_change',  # url name
        'method': 'POST',
        'args': [],
        'hooks':['func1' and  'func2']

    },
}