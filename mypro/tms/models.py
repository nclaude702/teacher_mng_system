from django.db import models

class Teacher(models.Model):
    tname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    leave_record = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tname


class Users(models.Model):
    names = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'userss'



