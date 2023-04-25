from django.shortcuts import render
from django.views import generic
from .models import Vzdelani, Projekt, PracovniZkusenost

# Create your views here.


class VzdelaniView(generic.ListView):

    template_name = "webresume/vzdelani.html"
    context_object_name = "vzdelani"

    def get_queryset(self):
        return Vzdelani.objects.all().order_by("-id")


class PracovniZkusenostView(generic.ListView):

    template_name = "webresume/pracovni_zkusenosti.html"
    context_object_name = "pracovni_zkusenosti"

    def get_queryset(self):
        return PracovniZkusenost.objects.all().order_by("-id")


class ProjektView(generic.ListView):

    template_name = "webresume/portfolio.html"
    context_object_name = "projekty"

    def get_queryset(self):
        return Projekt.objects.all().order_by("-id")


class DovednostiView(generic.TemplateView):

    template_name = "webresume/dovednosti.html"
    context_object_name = "dovednosti"


class ZajmyView(generic.TemplateView):

    template_name = "webresume/zajmy.html"
    context_object_name = "zajmy"


class OMneView(generic.TemplateView):

    template_name = "webresume/o_mne.html"
    context_object_name = "o_mne"
