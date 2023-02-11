from django.db import models

# Create your models here.
class Jobpost(models.Model):
    jobId = models.AutoField(primary_key=True)
    jobName=models.CharField(max_length=122)
    jobDescription=models.CharField(max_length=10000)

    

    def __str__(self):
        return self.jobName


class Notification(models.Model):
    Addnotification=models.CharField(max_length=1000)


    def __str__(self):
        return self.Addnotification