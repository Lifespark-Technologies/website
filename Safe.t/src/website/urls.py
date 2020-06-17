"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

#import home_view from pages
from pages.views import home_view, about_view, volunteer_view, hiw_view, faq_view, donate_view, community_view

urlpatterns = [
	#home_view path
    path('', home_view, name='home'),
    #about_view path
    path('about/', about_view, name ='about'),
    #volunteer_view path
    path('volunteer/', volunteer_view, name ='volunteer'),
    #hiw_view path
    path('how-it-works/', hiw_view, name ='how-it-works'),
    #faq_view path
    path('faq/', faq_view, name ='faq'),
    #donate_view path
    path('donate/', donate_view, name ='donate'),
    #community_view path
    path('community/', community_view, name ='community'),
    #admin path (general)
    path('admin/', admin.site.urls),
]
