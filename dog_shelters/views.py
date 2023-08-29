from django.shortcuts import render, get_object_or_404
from . import models #importation des gabarits
# TODO: Import generic views
from django.views import generic

# charger tous les refuges
# créez l’objet de contexte pour le gabarit 
# affichez le gabarit pour l’utilisateur
def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

#charger un refuge selon son pk (clé primaire)
#créez l’objet de contexte pour le gabarit,
# affichez le gabarit pour l’utilisateur.
def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

#création de la vue générique pour DogDetail
# définir le modèle, le template et l’objet de contexte.
class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'