
from django.contrib import admin
from django.urls import path, include
from studies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studies/', include('studies.urls')),
    path('', views.main_view, name='main_view'),
]
