from django.shortcuts import render,redirect,reverse,HttpResponse,Http404
from .models import TeaComponent
# Create your views here.
from django.core.files.storage import FileSystemStorage

def BaseView(request):
    if request.method == "GET":
        try:
           tea = TeaComponent.objects.all()
           return render(request,"tea/index.html",{"tea":tea})
        except TeaComponent.DoesNotExist:
            raise Http404
    return render(request,"tea/index.html",context = {"message":"added"})

def AddItem(request):
    if request.method == 'GET':
        return render(request,"tea/additem.html",context={"message": "thik hai"})
    elif request.method == 'POST' and request.FILES['myfile']:
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = TeaComponent()
        if data:
            data.name = name
            data.description = description
            data.price = price
            data.photo = uploaded_file_url
            data.save()
            return redirect(BaseView)
        return render(request,"tea/additem.html",context={"uploaded_file_url":uploaded_file_url})

def DeleteView(request,id):
    tea = TeaComponent.objects.get(pk=id)
    if request.method == 'POST':
        tea.delete()
        return redirect(BaseView)
    return render(request,'tea/deleteitem.html',{"tea":tea})

def DetailView(request,id):
    tea = TeaComponent.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'tea/detail.html',{"tea":tea})
    return render(request, 'tea/detail.html', {"tea": tea})