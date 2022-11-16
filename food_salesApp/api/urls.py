from django.urls import path, include

from food_salesApp.api.views import FoodApiViews

from rest_framework import routers
router = routers.DefaultRouter()
router.register("results", FoodApiViews, basename="results")


urlpatterns = [
    path("", include(router.urls)),
]
