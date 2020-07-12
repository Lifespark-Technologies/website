from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#homepage view
def home_view(request, *args, **kwargs): #args, keywordargs
	#return HttpResponse("<h1> Your Face</h1>") #String of html code
	return render(request, "home.html", {})
	
#about page view
def about_view(request, *args, **kwargs):
	#defines dictionary that is returned for render
	return render(request, "about.html", {})

#volunteer page view
def volunteer_view(request, *args, **kwargs):
	return render(request, "volunteer.html", {})

#how it works page view
def hiw_view(request, *args, **kwargs):
	return render(request, "how_it_works.html", {})

#faq page view
def faq_view(request, *args, **kwargs):
	return render(request, "faq.html", {})

#donation page view
def donate_view(request, *args, **kwargs):
	return render(request, "donate.html", {})

#community page view
def community_view(request, *args, **kwargs):
	return render(request, "community.html", {})

#join us page view
def ju_view(request, *args, **kwargs):
	return render(request, "join_us.html", {})
