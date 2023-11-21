from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
