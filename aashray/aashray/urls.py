"""aashray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('donor/',views.donate_plasma, name='donate_plasma'),
    path('locations/<slug:the_slug>/',views.loc, name='loc'),
    path('others/',views.others, name='others'),
    path('resources/Oxygen/<slug:the_slug>/',views.oxygen, name='oxygen'),
    path('resources/Beds/<slug:the_slug>/',views.bed, name='bed'),
    path('resources/Plasma/<slug:the_slug>/',views.plasma, name='plasma'),
    path('resources/Medicines/<slug:the_slug>/',views.medicine, name='medicine'),
    path('helplines/',views.helplines, name='helplines'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
