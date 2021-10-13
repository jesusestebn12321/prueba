from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Book(models.Model):
	"""docstring for book"""
	title=models.CharField(max_length=50)
	publication_date=models.DateField(default=timezone.now)
	
	def __str__(self):
		return f'{self.title}'

class Comment(models.Model):
	"""docstring for comments"""
	text=models.CharField(max_length=50)
	books=models.ForeignKey(Book,null=True,blank=True,on_delete=models.CASCADE)
	user = models.ForeignKey(get_user_model(),null=True,blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return '{user} - {text}'.format(user=self.user,text=self.text)