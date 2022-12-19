from django.db import models

class StudentModel(models.Model):
    roll_no = models.PositiveSmallIntegerField(unique=True)
    pr_no = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    classs=models.CharField( max_length=50,blank=True, null=True)
    admissiondate=models.DateTimeField(blank=True, null=True)
    dob=models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    cat=models.CharField( max_length=50,blank=True, null=True)
    mobno=models.CharField(max_length=10,blank=True, null=True)
    email=models.EmailField( max_length=254,blank=True, null=True)
    address=models.CharField( max_length=50,blank=True, null=True)
    fathername= models.CharField(max_length=20,blank=True, null=True)
    mobno_father=models.CharField(max_length=10,blank=True, null=True)
    mothername= models.CharField(max_length=20,blank=True, null=True)
    mobno_mother=models.CharField(max_length=10,blank=True, null=True)
    parentsEmail=models.EmailField( max_length=254,blank=True, null=True)
    attendance = models.FloatField(default=0,blank=True, null=True)

    def __str__(self):
        return self.name


class SubjectModel(models.Model):
    subject_name = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name


class SubjectTakenModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
