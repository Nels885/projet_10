from django.urls import path

from . import views

app_name = "save"
urlpatterns = [
    path('my_foods/', views.my_foods, name="my_foods"),
    path('<int:search_id>/<int:subs_id>/', views.backup, name="backup"),
    path('<int:subs_id>/', views.delete, name="delete"),
]
