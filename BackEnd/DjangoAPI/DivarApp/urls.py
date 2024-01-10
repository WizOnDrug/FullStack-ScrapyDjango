from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^divar$', views.DivarApi),
    re_path(r'^divar/[0-9]+/$', views.DivarApi),
]
