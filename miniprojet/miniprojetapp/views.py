from django.shortcuts import render
from .models import Formation
from django.core.paginator import Paginator

#liste des formations+recherche.
def index(request):

    #formations = Formation.objects.all()
    formations = Formation.objects.get_queryset().order_by('id')
    template_name = 'miniprojetapp/index.html'
    # Search funtionality
    categorie = request.GET.get('categorie')
    if categorie != '' and categorie is not None:                             #For querysets questions please view the page
        formations =formations.filter(categorie__icontains = categorie) #https://sodocumentation.net/django/topic/1235/querysets
    #Paginator code & link 
    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(formations,4)
    page_number = request.GET.get('page')#extraction d'une page
    formations = paginator.get_page(page_number)

    return render(request,template_name,{'formations': formations})


def detail(request,obj_id):
    formation = Formation.objects.get(id=obj_id)
    return render(request,'miniprojetapp/detail.html',{'formation':formation})