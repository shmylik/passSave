from django.db import models

class Password(models.Model):
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    site = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return "login: " + self.login + ', site: ' + self.site