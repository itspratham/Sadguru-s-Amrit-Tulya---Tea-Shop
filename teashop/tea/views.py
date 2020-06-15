from django.shortcuts import render

# Create your views here.

def BaseView(request):
        return render(request,"tea/index.html",context = {"message":"added"})

def AddItem(request):
    if request.method == 'GET':
        return render(request,"",context={"message": "thik hai"})
    elif request.method == 'POST':

        return render(request,"",context={"message":"added a form"})