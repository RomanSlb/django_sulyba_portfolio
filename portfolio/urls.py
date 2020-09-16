from django.urls import path, include
from . import views
from .views import home_view, about_me
from .views import render_pdf_view


app_name = 'portfolio'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_me, name='about_me'),
    path('projects/', views.post_list, name='projects'),
    path('projects/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact_me_view, name='contact'),
    path('download', render_pdf_view, name='test-view'),
]
