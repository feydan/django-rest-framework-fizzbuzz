from django.db import models

class FizzBuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=256, blank=True, default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=256, blank=True, default='')

    class Meta:
        ordering = ('fizzbuzz_id','useragent','creation_date', 'message')