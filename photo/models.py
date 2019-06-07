from django.db import models


class Lifestyle(models.Model):
    lifestyle = models.ImageField(upload_to='images/')
    
class Portrait(models.Model):
    portrait = models.ImageField(upload_to='images/')
    

class Portrait_detail(models.Model):
    portait_id = models.ForeignKey(Portrait, models.SET_NULL, blank=True, null=True)
    portrait_detail = models.ImageField(upload_to='images/')



class Lifestyle_detail(models.Model):
    lifestyle_id = models.ForeignKey(Lifestyle, models.SET_NULL, blank=True, null=True)
    lifestyle_detail = models.ImageField(upload_to='images/')
     
    

    