from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def my_memories(request):
    return HttpResponse("Memories of Melvin")