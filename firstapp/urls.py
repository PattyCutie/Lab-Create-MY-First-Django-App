from django.urls import path
from . import views

urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    # Add another path object defining the URL pattern using '/date' prefix
    # <HINT> Add a date URL path 
    # rout="URL_path",view=="views.<add the function name>", name="add name"
    path(route='date', view=views.get_date, name='date'),
]
