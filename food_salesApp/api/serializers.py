from food_salesApp.models import Food

from rest_framework.serializers import ModelSerializer

class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        lookup_field = 'product'
