from django.shortcuts import render
from django.template import *

# Create your views here.
def en_about(request):
    return render(request, 'hfe/en/home/about.html')

def en_research(request):
    return render(request, 'hfe/en/home/research.html')

def en_curriculum(request):
    return render(request, 'hfe/en/home/curriculum.html')

def en_faculty(request):
    return render(request, 'hfe/en/home/faculty.html')

def en_main(request):
    return render(request, 'hfe/en/home/main.html')


def ko_about(request):
    return render(request, 'hfe/ko/home/about.html')

def ko_research(request):
    return render(request, 'hfe/ko/home/research.html')

def ko_curriculum(request):
    return render(request, 'hfe/ko/home/curriculum.html')

def ko_faculty(request):
    return render(request, 'hfe/ko/home/faculty.html')

def ko_main(request):
    return render(request, 'hfe/ko/home/main.html')

def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))