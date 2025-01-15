from django.urls import path,include
from . import views
from api.views import PstGet

urlpatterns = [
    path('',views.testing),
    path('alldata/', PstGet)
]