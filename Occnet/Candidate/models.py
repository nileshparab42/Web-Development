from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()
    time = models.DateField()

    def __str__(self):
        return self.name


class Job(models.Model):
    cname = models.CharField(max_length=300,primary_key=True)
    pimg =  models.TextField()
    banner =  models.TextField()
    vname = models.CharField(max_length=300)
    hname = models.CharField(max_length=300)
    hdesc = models.TextField()
    srtdesc = models.TextField()
    lngdesc = models.TextField()
    itime = models.DateField() 

    def __str__(self):
        return self.cname


class Application(models.Model):
    sr = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    vacancy = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name
