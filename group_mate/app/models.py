from django.db import models

# Create your models here.

class Schools(models.Model):
	name = models.CharField(max_length=50)
	email_address_key = models.CharField(max_length=50)

class Classes(models.Model):
	class_name = models.CharField(max_length=50)
	professor = models.CharField(max_length=50)
	section_numb = models.IntegerField()
	school = models.ForeignKey(Schools, on_delete=models.CASCADE)

class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	school = models.ForeignKey(Schools, on_delete=models.CASCADE)
	classes = models.ManyToManyField(Classes)


class Messages(models.Model):
	content = models.CharField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	numLikes = models.IntegerField()
	datetimeadded = models.DateTimeField(auto_now=False, auto_now_add=False)
	class_related = models.ForeignKey(Classes, on_delete=models.CASCADE)
