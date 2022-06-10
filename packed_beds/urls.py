from django.urls import path

from piping import views

app_name = 'packed_beds'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name="packed_beds_projects"),
]
