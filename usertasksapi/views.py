from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 
from .models import User,Task
from .serializers import UserSerializer,TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def api_users(request):
    #getting all users
    if request.method == 'GET': 
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)       

    #creating an user
    if request.method == 'POST':

        data = {
            'name': request.data.get('name') 
        }
        
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['DELETE'])
def api_user(request,id):

    try:
        user =  User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #deleting a single user 
    if request.method == 'DELETE':
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET','POST'])
def api_user_tasks(request,userid):

    try:
        user =  User.objects.get(id=userid)
        tasks = Task.objects.get(user=user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #getting all tasks of a single user 
    if request.method == 'GET': 
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)

    #creating a task
    if request.method == 'POST':

        data = {
            'description': request.data.get('description'),
            'user_id': userid,
            'status': request.data.get('status')  
        }

        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
 

@api_view(['GET','DELETE', 'PUT'])
def api_task(request,id):

    try:
        task = Task.objects.get(id=id) 
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    #deleting a single task 
    if request.method == 'DELETE':
         task.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)  

    #editing a single task      
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

 
         


def user(request): 
    #get the model info to be used in the html page
    context = {
        'list': User.objects.all(),
        'entity':'user',
        'title':"Listagem de Usuários",
        'entity_pt':User._meta.verbose_name,
        'is_task':False,
        'inputs':[
        		   {
                   "name":"name",
                   "name_pt":"Nome",
                   "type":"text",
                   "value":""
                   },        			
        		 ]  
    } 
     
    return render(request, 'templates/usertasksapi/content.html', context)


def usertasks(request,user_id):
 
    usertasks = Task.objects.select_related('user').filter(user_id=user_id)
    user_name = User.objects.filter(id=user_id).first().name 

    #verify if the user has tasks
    try:
        usertasks[0].id==None
        title = 'Tarefas de '+user_name 
    except Exception as e:    
        title = user_name+' não possui tarefas ainda' 
      
    #get the model info to be used in the html page
    context = {

            'list': usertasks,
            'entity':'task',
            'title':title,
            'is_task':True,
            'entity_pt':Task._meta.verbose_name,
            'inputs':[
                        {
                        "name":"description",
                        "name_pt":"Descrição",
                        "type":"text",
                        "value":""
                        },                  
                        {
                        "name":"user",
                        "name_pt":"Usuário",
                        "type":"hidden",
                        "value":user_id
                        } 
                     ] , 
            'user_name': user_name
        } 
  
    
    return render(request, 'templates/usertasksapi/content.html', context)