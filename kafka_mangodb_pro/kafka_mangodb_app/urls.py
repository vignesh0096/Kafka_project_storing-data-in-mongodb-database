from django.urls import path
from .views import ProduceData,ConsumeData

urlpatterns = [
    path('producer/', ProduceData.as_view()),
    path('consumer/', ConsumeData.as_view())
]