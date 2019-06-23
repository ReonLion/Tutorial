from django.db import models

# Create your models here.

class Students(models.Model):
    studentID = models.CharField(max_length=15)
    studentName = models.CharField(max_length=20)
    studentSchool = models.CharField(max_length=20)
    studentAcademy = models.CharField(max_length=20)
    studentGrade = models.DateTimeField()
    studentDorm = models.ForeignKey('Dorms', on_delete=models.DO_NOTHING)
    studentOnline = models.BooleanField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '%s-%s' % (self.studentName, self.studentID)

class Dorms(models.Model):
    schoolName = models.CharField(max_length=20)
    dormName = models.CharField(max_length=20)
    dormFloor = models.IntegerField()
    dormNo = models.IntegerField()
    dormLastUpdateTime = models.DateTimeField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return '%s-%d' % (self.dormName, self.dormNo)
