from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'academy/home.html')

def about(request):
    return render(request, 'academy/about.html')

def contact(request):
    return render(request, 'academy/contact.html')

def course(request):
    return render(request, 'academy/course.html')

def team(request):
    return render(request, 'academy/team.html')

def testimonial(request):
    return render(request, 'academy/testimonial.html')

def detail(request):
    return render(request, 'academy/detail.html')

def feature(request):
    return render(request, 'academy/feature.html')