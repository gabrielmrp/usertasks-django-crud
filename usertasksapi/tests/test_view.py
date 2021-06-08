from django.test import TestCase
from usertasksapi.models import User,Task


import json
from django.test import Client
from django.urls import reverse
from rest_framework import status
from usertasksapi.serializers import UserSerializer,TaskSerializer

client = Client()


class UserModelTestClass(TestCase):
    @classmethod
    def setUp(self):
        self.user_1 = User.objects.create(name='Cornélius')
        self.user_2 = User.objects.create(name='Urias')
        
        self.user_new = {  
            'name' : 'John' 
        }    


    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('api_users'))
        # get data from db
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_user(self): 
        response = client.post(
            reverse('api_users'),
            format='json',
            data=self.user_new,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user(self):
        response = client.delete(
            reverse('api_user', kwargs={'id': self.user_1.id})) 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        """def test_get_user(self):
        response = client.get(
            reverse('api_user', kwargs={'id': self.user_1.id}))
        user = User.objects.get(id=self.user_1.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        """

        

class UserTasksModelTestClass(TestCase):

    @classmethod
    def setUp(self):
        self.user_1 = User.objects.create(name='Cornélius',id=1)
        self.task_1 = Task.objects.create(description='Compras',user=self.user_1)
        
        self.task_status = { 
            'status': 'feito' 
        }

        self.task_new = { 
            'user_id' : self.user_1.id,
            'status' : 'pendente',
            'description' : 'Revisão'
        } 


    def test_get_all_tasks_of_user(self):
        response = client.get(
            reverse('api_user_tasks', kwargs={'userid': self.user_1.id}))
        tasks = Task.objects.get(user=self.user_1)
        serializer = TaskSerializer(tasks)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_delete_task(self):
        response = client.delete(
            reverse('api_task', kwargs={'id': self.task_1.id}))  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
         
 
    def test_edit_task(self):
        serializer = TaskSerializer(self.task_1)
        response = client.put(
            reverse('api_task', kwargs={'id': self.task_1.id}),
            format='json', 
            data = self.task_status,
            content_type='application/json'
         ) 
        self.assertEqual(response.data['status'],"feito") 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_task(self): 
        response = client.post(
            reverse('api_user_tasks', kwargs={'userid': self.task_new['user_id']}),
            format='json',
            data=self.task_new,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          
