from django.contrib import admin
from django.urls import path
from bmi_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.bmi_calculator, name="bmi_calculator"),
]
