from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, get_object_or_404
from .models import Course, Submission  # Import the relevant models
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('submit/<int:course_id>/', views.submit, name='submit'),
    path('show_exam_result/<int:course_id>/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
