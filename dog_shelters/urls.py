#les chemins pour les deux vues

from django.urls import path
from . import views
# TODO: Register detail view


urlpatterns = [
    path('', views.shelter_list, name='shelter_list'), # ('') chemin par défaut
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'), #enregistrement de la vue details
    # More patterns to come later
]