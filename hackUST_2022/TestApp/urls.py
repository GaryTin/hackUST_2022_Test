from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('toilet/', views.toilet, name='toilet'),
  path('success/', views.success, name='success'),
  path('personal/<slug:people_slug>',views.personal,name='personal'),

]