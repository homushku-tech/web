from rest_framework.serializers import ModelSerializer
from main.models import InformationResource

class OrderSerializer(ModelSerializer):

    class Meta:
        model = InformationResource
        fields = ['name', 'slug', 'description', 'image']

