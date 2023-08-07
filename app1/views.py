from django.shortcuts import render

def nag(request):
    return render(request,'nag.html')
