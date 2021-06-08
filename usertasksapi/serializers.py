from rest_framework import serializers
from .models import User,Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name'] 
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = ['description', 'status', 'user'] 

 		 