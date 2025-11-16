from django.contrib import admin
from django.urls import path
from vehiclesapp.views import create_view, list_view, update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_view, name='create_view'),  # Agregar name
    path('update/<int:id>/', update_view, name='update_view'),
    path('', list_view, name='list_view'),
]