from typing import Text
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage2/index.html")


def section(request, num):
    if 1<= num <=3:
        return HttpResponse( Text [num -1])
    else:
        raise Http404("No existe la seccion")

