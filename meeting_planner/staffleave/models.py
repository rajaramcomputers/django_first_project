from django.db import models

# Create your models here.
class staffdetails(models.Model):
    staffid = models.IntegerField()
    staffname = models.CharField(max_length=50)
    staffdept = models.CharField(max_length=15, default="")

    def __str__ (self):
        return f"{self.staffid}"

class leaveapplied(models.Model):
    staffid = models.ForeignKey(staffdetails, on_delete=models.CASCADE, related_name='rel')
    startdate = models.DateField()
    enddate = models.DateField()
    noofdays = models.IntegerField(default=None)
    leavebalance = models.IntegerField(default=None)

    def __str__ (self):
        return f"{self.staffid}"
