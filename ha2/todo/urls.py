from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('impressum/', views.impressum, name="impressum"),
    path('howto', views.howto, name="howto")
]