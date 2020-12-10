from django.shortcuts import render
from .models import *
# Create your views here.


def main(request):
    home_pg = Home.objects.all()
    menu = Menu.objects.all()
    context = {
        'home_pg': home_pg,
        'menu': menu,
    }
    return render(request, 'main/index.html', context)


def about(request):
    about_pg = About.objects.all()
    footer = Footer.objects.all()
    context = {
        'about_pg': about_pg,
        'footer': footer,
    }
    return render(request, 'main/about.html', context)


def work(request):
    work_pg = Work.objects.all()
    context = {'work_pg': work_pg}
    return render(request, 'main/work.html', context)