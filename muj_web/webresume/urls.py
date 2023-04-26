from django.urls import path
from . import views
from . import url_handler

urlpatterns = [
    path("/vzdelani/", views.VzdelaniView.as_view(), name="vzdelani"),
    path("/pracovni_zkusenosti/", views.PracovniZkusenostView.as_view(), name="pracovni_zkusenosti"),
    path("/portfolio/", views.ProjektView.as_view(), name="portfolio"),
    path("/dovednosti/", views.DovednostiView.as_view(), name="dovednosti"),
    path("/zajmy/", views.ZajmyView.as_view(), name="zajmy"),
    path("/o_mne/", views.OMneView.as_view(), name="o_mne"),
    path("/", url_handler.index_handler),
]
