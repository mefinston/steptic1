from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
   title = models.CharField(max_length=255)
   text = models.TextField()
   added_at = models.DateTimeField()
   rating = models.IntegerField()
   author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='question_author')
   likes = models.ManyToManyField(User, related_name='question_likes')
   class Meta:
      db_table='question'

class Answer(models.Model):
   text = models.TextField()
   added_at = models.DateTimeField()
   question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
   author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
   class Meta:
      db_table='answer'

