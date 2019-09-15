from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, './stock/index.html', {})


class StockPredict(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={'closing_price': 235.43, 'year': kwargs['year'], 'date': kwargs['day'], 'month': kwargs['month'] }, status=status.HTTP_200_OK) 
