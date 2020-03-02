#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import pickle
from config import settings
from src import identifier


class BaseModel:
    def save(self):
        """
        使用pickle将用户对象保存到文件
        :return:
        """
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb'))

# obj = Admin('root', 123)
# 将obj写入到db/admin目录
class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        """
        创建管理员对象
        :param username:
        :param password:
        :return:
        """
        # nid唯一ID，随机字符串
        #
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login(user, pwd):
        """
        管理员登陆，去遍历/db/admin/,pickle.load()
        for item 循环/db/admin/所有文件:
            obj = pickle.load(open(os.path.join(/db/admin/, item)))
            if user == obj.username and pwd == obj.password:
                return obj

        return None

        :param user: 管理员用户名
        :param pwd: 管理员密码
        :return: 如果登陆成功，获取管理员对象，否则 None
        """


class School(BaseModel):
    db_path = settings.SCHOOL_DB

    def __init__(self, name):
        self.nid = identifier.SchoolNid(School.db_path)
        self.schoolName = name
        self.income = 0

    def __str__(self):
        return self.schoolName

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(School.db_path)):
            obj = pickle.load(open(os.path.join(School.db_path, item), 'rb'))
            ret.append(obj)
        return ret


class Teacher(BaseModel):
    db_path = settings.TEACHER_DB

    def __init__(self, name, level):
        """
        :param name: 老师姓名
        :param level: 老师级别
        """

        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.teacherName = name
        self.teacherLevel = level
        self.__account = 0

# obj.courseName  课程名
# obj.coursePrice 课程价格
# obj.school_id表示学校唯一ID对象（） identifier.SchoolNid(School.db_path)
# obj.school_id.get_obj_by_uuid().schoolName 表示学校唯一ID对象（） identifier.SchoolNid(School.db_path)

class Course(BaseModel):
    db_path = settings.COURSE_DB

    def __init__(self, name, price, period, school_id):
        """
        :param name: 课程名
        :param price: 课程价格
        :param period: 课程周期
        :param school_id: 关联学校Id，学校ID具有get_obj_by_uuid方法，以此获取学校对象（其中包含学校信息）
        """
        self.nid = identifier.CourseNid(Course.db_path)
        self.courseName = name
        self.coursePrice = price
        self.coursePeriod = period
        self.schoolId = school_id

    def __str__(self):
        return "课程名：%s；课程价格：%s；课程周期：%s；所属学校：%s" % (
            self.courseName, self.coursePrice, self.coursePeriod, self.schoolId.get_obj_by_uuid().name, )

    @staticmethod
    def get_all_list():
        """
        获取所有课程对象
        """
        ret = []
        for item in os.listdir(os.path.join(Course.db_path)):
            obj = pickle.load(open(os.path.join(Course.db_path, item), 'rb'))
            ret.append(obj)
        return ret

# 语文id - Alexid
# 语文 - SB
# 体育 - Eric
# 英语 - Alex

class CourseToTeacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB

    def __init__(self, course_id, teacher_id):
        self.nid = identifier.CourseToTeacherNid(CourseToTeacher.db_path)
        self.courseId = course_id
        self.teacherId = teacher_id


    @staticmethod
    def course_teacher_list():
        pass

#  # 语文id - Alexid, # 体育 - Eric
class Classes(BaseModel):
    db_path = settings.CLASSES_DB

    def __init__(self, name, tuition, school_id, course_to_teacher_list):
        """
        班级
        :param name: 班级名
        :param tuition: 学费
        :param school_id: 学校NID
        :param course_to_teacher_list:  [CourseToTeacher,CourseToTeacher,]
        """
        self.nid = identifier.ClassesNid(Classes.db_path)
        self.name = name
        self.tuition = tuition
        self.schoolId = school_id
        self.courseToTeacherList = course_to_teacher_list


class Score:
    """
    成绩单
    """

    def __init__(self, student_id):
        self.studentId = student_id
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid, None)


class Student(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, name, age, classes_id):
        self.nid = identifier.StudentNid(Student.db_path)
        self.name = name
        self.age = age
        self.classesId = classes_id
        self.score = Score(self.nid)
        # self.score = {
        #     '# 体育 - Eric'： 69，
        #     '语文id - Alexid'： 69，
        # }
    @staticmethod
    def register():
        pass


