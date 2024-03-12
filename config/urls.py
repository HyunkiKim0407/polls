from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

]