from django.urls import path
from . import views

app_name = "pages"

utlpatterns = [
    path(" ", views.HomePageView.as_view(), name="home"),


]