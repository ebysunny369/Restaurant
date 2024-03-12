from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def menu(request):
    return render(request,'Menu.html')
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
