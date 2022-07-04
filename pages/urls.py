from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work',views.work ,name='work'),
    path('cv',views.cv ,name='cv'),
    path('contact',views.contact ,name='contact'),
    path('<int:id>',views.projec,name='project_detail'),
    
]
