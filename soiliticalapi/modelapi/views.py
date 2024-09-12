import os
import pickle
import bz2
import numpy as np
from django.conf import settings
from sklearn.preprocessing import StandardScaler
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PredictionInputSerializer


class PredictionAPIView(APIView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_encoder = self.load_label_encoder(
            os.path.join(settings.BASE_DIR, 'modelapi', 'ml_models', 'label_encoder.pkl'))
        self.model = self.load_model(
            os.path.join(settings.BASE_DIR, 'modelapi', 'ml_models', 'random_forest_model.pbz2'))
        self.scaler = StandardScaler()
    
    def load_label_encoder(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def load_model(self, filename):
        with bz2.BZ2File(filename, 'rb') as model_file:
            return pickle.load(model_file)

    def post(self, request, *args, **kwargs):
        serializer = PredictionInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            values_list = [[data['N'], data['P'], data['K'], data['Humidity'], data['Temp'], data['PH']]]
            pred = self.model.predict(values_list)

            prediction = self.label_encoder.inverse_transform((pred))[0]
    
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelInfoAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = self.load_model(
            os.path.join(settings.BASE_DIR, 'modelapi', 'ml_models', 'random_forest_model.pbz2'))

    def load_model(self, filename):
        with bz2.BZ2File(filename, 'rb') as model_file:
            return pickle.load(model_file)

    def get(self, request, *args, **kwargs):
        model_info = {
            "model_type": type(self.model).__name__,
            "n_features": self.model.n_features_in_,
            "n_estimators": self.model.n_estimators,
            "max_depth": self.model.max_depth,
            "feature_importances": self.model.feature_importances_.tolist()
        }

        return Response({'model_info': model_info}, status=status.HTTP_200_OK)
