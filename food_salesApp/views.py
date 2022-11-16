from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from food_salesApp.models import Food

# Create your views here.

class FoodListView(ListView):
    model = Food

class FoodDetailView(DetailView):
    model = Food

class FoodCreateView(CreateView):
    model = Food
    fields = "__all__"

class FoodUpdateView(UpdateView):
    model = Food
    fields = "__all__"
class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('list')
