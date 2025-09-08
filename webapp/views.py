from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to KDFitness home page.")

def contactus(request):
    return HttpResponse("Drop us an email at hello@kdfitness.com to find out more")

def login(request):
    return HttpResponse("Enter your username and password to login.")