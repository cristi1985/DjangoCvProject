from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_data', views.submit_data, name='submit data'),
    path('<int:job_id/job_name/', views.job_name, name='job_name'),
]