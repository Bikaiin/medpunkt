from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('queue/<int:user_id>', views.queue_view, name='queue_view'),
]