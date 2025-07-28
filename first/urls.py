"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    # agar ye path match hota h to myapp.url pr bhej do--(agar path blank hai to app url ke pass jaa wo deside karega kya karna hai)
    path('', include('myapp.urls')),

]

# change django adminstration
admin.site.site_header = "LEAF DISEASE DETECTION"
admin.site.site_title = "LEAF DISEASE DETECTION Admin Portal"
admin.site.index_title = "Welcome to LEAF DISEASE DETECTION Researcher Portal"
