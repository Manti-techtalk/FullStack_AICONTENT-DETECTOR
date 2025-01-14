from rest_framework import serializers
from api.models import User,TextSubmission,AiModelData,Analysis

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TextSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSubmission
        fields = '__all__'

class AiModelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiModelData
        fields = '__all__'

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

