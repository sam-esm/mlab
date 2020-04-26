from django.test import TestCase
from .models import MTest
from datetime import datetime,date

class MTestsTest(TestCase):
    def setUp(self):
        MTest.objects.create(reception_code=12345,
            reception_date = datetime.now(),answer_date=date(2002, 12, 31),deliver_sample=True) 
        print(MTest.objects.all())

    def test_string_representation(self):
        print(MTest.objects.all())
        mt = MTest.objects.get(reception_code=12345)
        self.assertEqual(str(mt.reception_code),mt.__str__())