from django.test import TestCase
 
from usertasksapi.models import User,Task


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(name='Cornélius',id=1)
        Task.objects.create(description='Cornélius Task',status='pendente',user=user,id=1)
        pass

    def setUp(self): 
        pass
   
    def test_user_name_label(self):
        user = User.objects.get(id=1)
        label = user._meta.get_field('name').verbose_name
        self.assertEquals(label, 'name')  

    def test_usertask_description_label(self):
        task = Task.objects.get(id=1)
        label = task._meta.get_field('description').verbose_name
        self.assertEquals(label, 'description')  

    def test_usertask_status_label(self):
        task = Task.objects.get(id=1)
        label = task._meta.get_field('status').verbose_name
        self.assertEquals(label, 'status')                  


    def test_user_name_max_length(self):
        #65 characters
        max_length = User._meta.get_field('name').max_length
        self.assertEquals(max_length, 64)

    def test_user_name_description_length(self):
        #65 characters
        max_length = Task._meta.get_field('description').max_length
        self.assertEquals(max_length, 1024)

    def test_user_name_status_length(self):
        #65 characters
        max_length = Task._meta.get_field('status').max_length
        self.assertEquals(max_length, 16)     

    def test_task_verbose_name(self):
        task = Task.objects.get(id=1)
        verbose_name = task._meta.verbose_name
        self.assertEquals(verbose_name, 'Tarefa')             

    def test_user_verbose_name(self):
        user = User.objects.get(id=1)
        verbose_name = user._meta.verbose_name
        self.assertEquals(verbose_name, 'Usuário')          

    # DELETION 

    def test_user_delete(self):  
        user = User.objects.get(id=1)  
        del_user = user.delete()
        self.assertFalse(User.objects.filter(id=1).exists())

    def test_task_delete(self):  
        task = Task.objects.get(id=1)  
        del_task = task.delete()
        self.assertFalse(Task.objects.filter(id=1).exists())        

    def test_user_task_delete(self):  
        user = User.objects.get(id=1)
        task = Task.objects.get(user=user)  
        del_user = user.delete()
        self.assertFalse(Task.objects.filter(user=user).exists())
