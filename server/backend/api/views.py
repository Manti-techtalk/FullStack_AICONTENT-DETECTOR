from django.shortcuts import render
from django.http import HttpResponse
from api.models import User, Analysis, AiModelData, TextSubmission
from api.serializers import UserSerializer, AnalysisSerializer, AiModelDataSerializer, TextSubmissionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST', 'GET'])
def PstGet(request):
    if request.method == 'GET':
        serializers = {
            'users': UserSerializer(User.objects.all(), many=True).data,
            'analyses': AnalysisSerializer(Analysis.objects.all(), many=True).data,
            'aimodeldata': AiModelDataSerializer(AiModelData.objects.all(), many=True).data,
            'textsubmissions': TextSubmissionSerializer(TextSubmission.objects.all(), many=True).data
        }
        return Response(serializers)

    if request.method == 'POST':
        response_data = {}
        serializers = {
            'users': UserSerializer(data=request.data),
            'analyses': AnalysisSerializer(data=request.data),
            'aimodeldata': AiModelDataSerializer(data=request.data),
            'textsubmissions': TextSubmissionSerializer(data=request.data)
        }
        for key, serializer in serializers.items():
            if serializer.is_valid():
                serializer.save()
                response_data[key] = serializer.data
            else:
                return Response(serializer.errors, status=400)
                
        return Response(response_data, status=201)


def testing(request):
    return HttpResponse('<h1>Testing api home page</h1>')