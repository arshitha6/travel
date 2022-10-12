from django.shortcuts import render

from .  models import place
from .  models import new_place


# Create your views here.
def demo(request):
    obj=place.objects.all()
    new_obj = new_place.objects.all()
    return render(request, "index.html",{'result':obj,'result2':new_obj})
