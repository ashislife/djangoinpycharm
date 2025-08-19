
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    # (ye wahi blank page hai jo website urls ke blank page se match kr rhi hai jo website urls ne bheja tha )
    # ab ye views ko forward kr dega kahega ki index naam ka fun bna or kaam kr
    path("", views.index, name='home'),

    # (agar / use karke about click karna ho to ye likho)
    # ye forward karega views.py ko
    path("about", views.about, name='about'),

    # ye view page me service ko req karega
    path("service", views.service, name='service'),

    path("contact", views.contact, name='contact'),

    path("treatment", views.treatment, name='treatment'),

    path("patato", views.patato, name='patato'),

    path("tamato",views.tamato,name='tamato'),






]
