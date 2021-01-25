from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

from .models import User,Task
from .serializers import UserSerializer,TaskSerializer
#from .viewsets import UserViewset,TaskViewset,TaskUserViewset

def user(request):
    users = User.objects.all()   
    fields = User._meta.fields
    modelname = 'User'
    #str(f.split('usertasksapi.'+entity)[0]) if 'id' not in f
    context = {
        'list': users,
        'entity':'user',
        'title':"Listagem de Usuários",
        'entity_pt':User._meta.verbose_name,
        'is_task':False,
        'inputs':[
        			{"name":"name","name_pt":"Nome","type":"text","value":""},        			
        		  ]  
    } 
    template = loader.get_template('templates/usertasksapi/index.html')      
    return HttpResponse(template.render(context, request))

"""def task(request):
    tasks = Task.objects.all()   
    fields =  Task._meta.fields
    modelname = 'Task'

    context = {
        'list': tasks,
        'entity':'task',
        'entity_pt':'Usuário',
        'inputs':{
        			"description":"",        			
        			"user_id":user_id,
        			"status":"pendente",
        		 }        
    } 
    template = loader.get_template('templates/usertasksapi/index.html')
    return HttpResponse(template.render(context, request))"""

def usertasks(request,user_id):

 
    usertasks = Task.objects.select_related('user').filter(user_id=user_id)
 
    inputs = [
                    {"name":"description","name_pt":"Descrição","type":"text","value":""},                  
                    {"name":"user","name_pt":"Usuário","type":"hidden","value":user_id} 
             ] 

    user_name = User.objects.filter(id=user_id).first().name             
    try:
        usertasks[0].id==None
        title = 'Tarefas de '+user_name
        
        user_name = usertasks.first().user.name 
    except Exception as e:         
        
        title = user_name+' não possui tarefas ainda' 
     
        
    
    
    entity_pt = Task._meta.verbose_name
    context = {

            'list': usertasks,
            'entity':'task',
            'title':title,
            'is_task':True,
            'entity_pt':entity_pt,
            'inputs':inputs, 
            'user_name': user_name
        } 



    template = loader.get_template('templates/usertasksapi/index.html')
    return HttpResponse(template.render(context, request))