# modelapi/serializers.py
from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    N = serializers.FloatField()
    P = serializers.FloatField()
    K = serializers.FloatField()
    PH = serializers.FloatField()
    Humidity = serializers.FloatField()
    Temp = serializers.FloatField()
