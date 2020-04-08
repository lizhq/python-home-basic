from django.db import models


class Classes(models.Model):
    caption = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32,null=True)
    cls = models.ForeignKey('Classes')


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField('Classes')


class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class Province(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32)
    pro = models.ForeignKey("Province")
    def __str__(self):
        return self.name

class Xian(models.Model):
    name = models.CharField(max_length=32)
    cy = models.ForeignKey("City")


class Book(models.Model):
    name =models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=32)
    m = models.ManyToManyField('Book')

    def __str__(self):
        return self.name

#
# class A_to_B(models.Model):
#     bid = models.ForeignKey(Book)
#     aid = models.ForeignKey(Author)
#
#     class Meta:
#         unique_together = (
#             ('bid','aid'),
#         )