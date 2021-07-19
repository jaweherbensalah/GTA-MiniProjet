
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Formation


# Register your models here.
admin.site.site_header="Site de formations"
admin.site.site_title="GTA"
admin.site.index_title="Gestion des formations"


class FormationsAdmin(admin.ModelAdmin):
    def makeActive(self,request,queryset):
        queryset.update(etat=True)
    def makeInActive(self,request,queryset):
        queryset.update(etat=False)
    
    makeActive.short_description="Changer l'état à active"
    makeInActive.short_description="Changer l'état à inactive"
    list_display = ('titre','categorie','etat','prix','description','logo')
    search_fields=('titre','categorie','prix','etat')#créer une barre de recherche pour l'admin
   # list_editable=('titre','categorie','etat','prix','description')
admin.site.register(Formation, FormationsAdmin)