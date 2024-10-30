from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^dashboard/records$", views.Dashboard.as_view(), name="dashboard"),
]
