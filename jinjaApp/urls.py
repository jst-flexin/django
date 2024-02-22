from django.urls import path
from jinjaApp import views

urlpatterns = [

    path('',views.home,name='my_index'),
    path('contact/',views.contact, name='my_contact'),
    path('about/',views.about, name='my_about'),
    path('gallery/',views.gallery, name='my_gallery'),
]