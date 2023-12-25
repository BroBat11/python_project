# Import necessary modules from Django REST Framework
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Import the Product model from the current module or package
from .models import Product

class bibloSerializer(serializers.ModelSerializer):
    # Hidden field for the user attribute with the default value set to the currently authenticated user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # Meta class provides metadata for the serializer
    class Meta:
        model = Product
        # Include all fields of the Product model in the serialized output
        fields = "__all__"
