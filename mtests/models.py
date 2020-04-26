from django.contrib.auth import get_user_model
from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class MTest(TimeStampedModel):
    """
        Medical Test model for every test response including reception code,
        answer date,reception dateand lab information..
    """
    reception_code = models.IntegerField(" کد پذیرش ",max_length=32,unique=True)
    reception_date =  models.DateField(" تاریخ پذیرش ",max_length=32)
    answer_date = models.DateField("تاریخ پاسخ",max_length=32)
    tests_file = models.FileField("فایل آزمایش",upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    response_file = models.FileField("فایل پاسخ",upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    Appendix_file = models.FileField("فایل ضمیمه",upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    deliver_sample = models.BooleanField("تحویل نمونه",default=False)
    response = models.BooleanField("پاسخ",default=False)
    approve_response = models.BooleanField("تایید پاسخ",default=False)
    def __str__(self):
        return "{}".format(self.reception_code)
    
