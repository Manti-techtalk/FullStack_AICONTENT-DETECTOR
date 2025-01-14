from django.contrib import admin
from api.models import User,TextSubmission,Analysis,AiModelData

# Register your models here.
admin.site.register(User)
admin.site.register(TextSubmission)
admin.site.register(Analysis)
admin.site.register(AiModelData)