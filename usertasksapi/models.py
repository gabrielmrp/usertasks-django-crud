from django.db import models

class User(models.Model):
	name = models.CharField(max_length=64)
	class Meta:
		verbose_name = "Usuário"


class Task(models.Model):
	description = models.CharField(max_length=1024,null=True)
	status = models.CharField(max_length=16,default="pendente")
	user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
	class Meta:
		verbose_name = "Tarefa"
