from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Food, FoodCategory
from .serializers import FoodListSerializer

class FoodListView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.all().exclude(name_ua="Додатки")

        foods = Food.objects.filter(is_publish=True)

        for category in categories:
            category.foods = foods.filter(category=category)

        serialized_data = FoodListSerializer(categories, many=True)

        return Response(serialized_data.data, status=200)
