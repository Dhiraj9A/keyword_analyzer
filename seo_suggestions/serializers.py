from rest_framework import serializers


class AnalyzeSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)