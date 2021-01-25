from usertasksapi.viewsets import UserViewset,TaskViewset
from rest_framework import routers
from usertasksapi import views
router = routers.DefaultRouter()
router.register('user',UserViewset)
router.register('task',TaskViewset)
#router.register('/a',views.index)


# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive