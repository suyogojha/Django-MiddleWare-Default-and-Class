from django.shortcuts import render,HttpResponse



def home(request):
    print("i am view")
    return HttpResponse("this is home page")