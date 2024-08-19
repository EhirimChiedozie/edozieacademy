from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='academy_home'),
    path('about/', views.about, name='academy_about'),
    path('contact/', views.contact, name='academy_contact'),
    path('course/', views.course, name='academy_course'),
    path('team/', views.team, name='academy_team'),
    path('testimonial/', views.testimonial, name='academy_testimonial'),
    path('detail/', views.detail, name='academy_detail'),
    path('feature/', views.feature, name='academy_feature'),
]