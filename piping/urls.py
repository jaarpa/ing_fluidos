from django.urls import path

from piping import views

app_name = 'piping'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name="piping_projects"),
    path('add/', views.ProjectCreateView.as_view(), name="add_project"),
    path(
        'project/<int:pk>/', views.ProjectDetailView.as_view(),
        name="project_detail"
    ),
    path(
        'project/<int:pk>/delete/', views.ProjectDeleteView.as_view(),
        name="delete_project"
    ),
]
