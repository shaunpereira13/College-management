from django.db import models

class StudentModel(models.Model):
    roll_no = models.PositiveSmallIntegerField(unique=True)
    pr_no = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    attendance = models.FloatField(default=0)
    def __str__(self):
        return self.name



class SubjectModel(models.Model):
    subject_name = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name


class SubjectTakenModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
