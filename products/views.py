from django.views import View
from django.http import HttpResponse
# Create your views here.


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1> Welcome to KdFitness, friend! </h1>")
class SupplementView(View):
    def get(self,request):
        return HttpResponse("<h2> Information of Supplements on Sale. </h2>")
class SportsWearView(View):
    def get(self,request):
        return HttpResponse("<h2> Sportswear Information on Sale. </h2>")
class RacquetsView(View):
    def get(self, request):
        return HttpResponse("<h2> Racquet Information on Sale. </h2>")
class WeightsView(View):
    def get(self,request):
        return HttpResponse("<h2> Weight Infromation on sale. </h2>")
class MealPortionPlansView(View):
    def get(self,request):
        return HttpResponse("<h2> Meal Portion Plans Information on sale. </h2>")
class CustomerServiceView(View):
    def get(self,request):
        return HttpResponse("<p>Contact us at hello@kdfitness.com or call + 65 6712 1239/ + 971 341 3478 123 to track delivery of shipment and for bulk purchases.</p>")