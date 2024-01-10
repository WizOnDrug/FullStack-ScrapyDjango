from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^jabama$', views.JabamaApi),
    re_path(r'^jabama/[0-9]+/$', views.JabamaApi),
]
