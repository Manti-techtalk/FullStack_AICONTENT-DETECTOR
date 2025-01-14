from django.shortcuts import render
from django.http import HttpResponse
from api.models import User,Analysis,AiModelData,TextSubmission
from api.serializers import UserSerializer,AnalysisSerializer,AiModelDataSerializer,TextSubmissionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.







def testing(request):
    return HttpResponse('<h1>Testing API</h1>')