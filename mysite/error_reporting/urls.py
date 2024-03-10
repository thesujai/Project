from django.conf.urls import url
from . import views

app_name = 'error_reporting'

urlpatterns = [
    # Add your URL patterns here
    # Example: path('example/', views.example_view, name='example'),
    url('', views.error_report, name='error_report'),
]