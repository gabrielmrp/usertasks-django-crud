from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 
# Create your views here.

from .models import User,Task
from .serializers import UserSerializer,TaskSerializer
 
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
    template = loader.get_template('templates/usertasksapi/content.html')      
    return HttpResponse(template.render(context, request))

 
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
  
    template = loader.get_template('templates/usertasksapi/content.html')
    return HttpResponse(template.render(context, request))

 