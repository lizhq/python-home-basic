# #__author:  Administrator
# #date:  2016/12/2
#
# ### 1、首先登陆任何页面，获取cookie
# import requests
#
# i1 = requests.get(url="http://dig.chouti.com/help/service")
#
# ### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
# i2 = requests.post(
#     url="http://dig.chouti.com/login",
#     data={
#         'phone': "8615131255089",
#         'password': "woshiniba",
#         'oneMonth': ""
#     },
#     cookies=i1.cookies.get_dict()
# )
#
# ### 3、点赞（只需要携带已经被授权的gpsd即可）
# gpsd = i1.cookies.get_dict()['gpsd']
# i3 = requests.post(
#     url="http://dig.chouti.com/link/vote?linksId=9365296",
#     cookies={'gpsd': gpsd}
# )
# print(i3.text)



#
#
# import datetime
# import json

# li = [
#     {'id':1, 'name': 'root'},
#     {'id':1, 'name': 'root'},
#     {'id':1, 'name': 'root'},
#     {'id':1, 'name': 'root'},
#     {'id':1, 'name': 'root'},
# ]
# import json
# from datetime import date
# from datetime import datetime
#
# class JsonCustomEncoder(json.JSONEncoder):
#     def default(self, field):
#
#         if isinstance(field, datetime):
#             return field.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(field, date):
#             return field.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, field)
#
# li = [
#     {'id':1, 'name': 'root', 'ctime': datetime.now()},
#     {'id':2, 'name': 'root', 'ctime': datetime.now()},
#     {'id':3, 'name': 'root', 'ctime': datetime.now()},
#     {'id':4, 'name': 'root', 'ctime': datetime.now()},
# ]
#
# v = json.dumps(li,cls=JsonCustomEncoder)
# print(v)















