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
        'project/<int:pk>/update/', views.ProjectUpdateView.as_view(),
        name="update_project"
    ),
    path(
        'project/<int:pk>/delete/', views.ProjectDeleteView.as_view(),
        name="delete_project"
    ),

    path(
        'project/accessory/add/',
        views.ProjectAccessoryCreateView.as_view(), name="add_accessory"
    ),
    path(
        'project/accessory/<int:pk>/delete/',
        views.ProjectAccessoryDeleteView.as_view(), name="delete_accessory"
    ),
]
