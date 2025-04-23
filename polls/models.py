from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model): 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"{self.question_text} {self.pub_date.isoformat()}"

    def publish_recent(self): 
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model): 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question} {self.votes} {self.choice_text}"