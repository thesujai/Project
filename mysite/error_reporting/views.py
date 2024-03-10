from django.shortcuts import render, HttpResponse

# Create your views here.
def error_report(request):
    x = 1/0
    return HttpResponse("Error reporting view.")