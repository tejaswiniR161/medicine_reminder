from django.db import models
from django.contrib.auth.models import User

class tablet(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    tablet_time=models.CharField(max_length=600,default="")
    
    def __str__(self):
        return '<%s %s>'%(self.uid, self.tablet_time)