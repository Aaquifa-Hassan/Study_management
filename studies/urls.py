# studies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),  # Root/homepage URL
    path('add/', views.add_study, name='add_study'),  # Add study view
    path('view/<int:study_id>/', views.view_study, name='view_study'),  # View a specific study
    path('edit/<int:study_id>/', views.edit_study, name='edit_study'),  # Edit a study
    # path('delete/<int:study_id>/', views.delete_study, name='delete_study'),  # Delete a specific study
    path('delete_selected/', views.delete_selected_studies, name='delete_selected_studies'),  # Delete selected studies
]