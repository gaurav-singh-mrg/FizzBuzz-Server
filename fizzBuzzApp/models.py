from django.db import models


class RequestStat(models.Model):
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    str1 = models.CharField(max_length=255)
    str2 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
