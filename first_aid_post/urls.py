from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('queue/<int:user_id>', views.queue_view, name='queue_view'),
    path('main', views.main_view, name='main_view'),
    path('patient/curent', views.patient_view, name='patient_view'),
    path('patient/next', views.patientnext_view, name='patientnext_view'),
    path('patient/search', views.search_view, name='search_view'),
    path('patient/search/<int:user_id>', views.s_patient_view, name='s_patient_view'),
    path('report/params', views.params_view, name='params_view'),
    path('report', views.report_view, name='report_view'),
    
]