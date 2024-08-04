from django.db import models
from django.utils import timezone 
# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=20,unique = True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return self.code
    def is_valid(self):
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to
        