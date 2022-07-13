from django.shortcuts import render
from barta.models import Bartas,Categorys,Singlenotice

# Create your views here.

def Bartahome(request):
    lastbarta = Bartas.objects.last()
    barta = Bartas.objects.exclude(id=lastbarta.id).all().order_by("-id")
    categories = Categorys.objects.all()
    single_notice = Singlenotice.objects.all().order_by('-id')[:10]

    context = {
        'barta':barta,
        'lastbarta':lastbarta,
        'categories':categories,
        'single_notice':single_notice,
    }
    return render(request, 'barta/bartahome.html', context)

def allSingleNotice(request):
    all_notice = Singlenotice.objects.all().order_by('-id')
    
    context ={
        "all_notice" : all_notice,
    }
    
    return render(request,"barta/all_notice.html",context)
    
def SinglePost(request,catslug,id):
    barta = Bartas.objects.get(id=id)
    categories = Categorys.objects.all()
    context = {'barta':barta,'categories':categories,}
    return render(request, 'barta/singlepost.html',context)

def CategoryPost(request,catslug):
    category = Categorys.objects.get(slug=catslug)
    
    categories = Categorys.objects.all()

    barta = Bartas.objects.filter(category=category).order_by("-id")
    
    
    context={
        'barta':barta,
        'categories':categories,
        'category':category,
        
        
    }
    return render(request, 'barta/categorypost.html',context)
