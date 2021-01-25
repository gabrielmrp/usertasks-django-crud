from rest_framework import viewsets
from . import models
from . import views
from . import serializers

class UserViewset(viewsets.ModelViewSet):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer


class TaskViewset(viewsets.ModelViewSet):
	queryset = models.Task.objects.all()
	serializer_class = serializers.TaskSerializer
	 