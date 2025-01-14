from django.contrib import admin
from api.models import User,TextSubmission,Analysis,AiModelData

# Register your models here.
admin.site.register(User,TextSubmission,Analysis,AiModelData)