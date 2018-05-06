from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_data', views.submit_data, name='submit data'),
    path('<int:applicant_id/applicant_cv/', views.applicant_cv, name='applicant cv'),
]