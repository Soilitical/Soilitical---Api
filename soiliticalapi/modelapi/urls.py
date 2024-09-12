from django.urls import path
from .views import PredictionAPIView, ModelInfoAPIView

urlpatterns = [
    path('predict/', PredictionAPIView.as_view(), name='predict'),
    path('model-info/', ModelInfoAPIView.as_view(), name='model_info'),
]
