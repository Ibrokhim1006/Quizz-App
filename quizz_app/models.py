from django.db import models
from django.contrib.auth.models import User

class Section_test(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Questions(models.Model):
    section_id = models.ForeignKey(Section_test,on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    option_one = models.CharField(max_length=120)
    option_two = models.CharField(max_length=120)
    option_three = models.CharField(max_length=120, blank=True)
    option_four = models.CharField(max_length=120, blank=True)
    answer = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question