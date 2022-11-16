from food_salesApp.models import Food
from food_salesApp.api.serializers import FoodSerializer
from rest_framework.pagination import PageNumberPagination
# from food_salesApp.pagination import ChangePaginationProperties

from rest_framework.viewsets import ModelViewSet

class FoodApiViews(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    search_fields = ('^product',)
		
