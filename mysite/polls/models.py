from __future__ import unicode_literals
from django.db import models

from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


@python_2_unicode_compatible
class Cpudata(models.Model):
    brand = models.CharField(max_length=20)
    gen = models.CharField(max_length=50)
    insurance = models.BooleanField(default=False)
    years = models.IntegerField(default=2558)
    price = models.FloatField(default=5000)

    def __str__(self):
        return '%s,%s,%f' % (self.brand, self.gen, self.price)