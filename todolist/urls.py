

#from django.contrib import admin
#from django.urls import include, path
#from rest_framework import routers
#from todolist.api import views

#router = routers.DefaultRouter()
#router.register(r'tasks', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('', include(router.urls)),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]

from django.contrib import admin
from django.urls import path, include
from todolist.api import views

urlpatterns = [
    path('', include('todolist.api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('todolist.api.urls')),
    path('<count>/', views.DetailTodo.as_view())

]
 