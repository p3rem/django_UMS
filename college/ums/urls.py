from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('about', views.about, name='about'),
    path('add_about', views.add_about, name='add_about'),
    path('edit_about/<int:id>', views.edit_about, name='edit_about'),
    path('delete_about/<int:id>', views.delete_about, name='delete_about'),
    path('contact', views.contact, name='contact'),
    path('view_contact', views.view_contact, name='view_contact'),
    path('register', views.register),
    path('student_entry', views.student_entry),
    path('student', views.student),
]