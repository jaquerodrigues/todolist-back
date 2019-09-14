from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
 path('', include('todolist.api.urls')),
    path('admin/', admin.site.urls),
     path('api/', include('todolist.api.urls'))
]