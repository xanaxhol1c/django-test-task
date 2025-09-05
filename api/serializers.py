from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Food, FoodCategory

class FoodSerializer(ModelSerializer):
    additional = SlugRelatedField(many=True, read_only=True, slug_field='name_ua')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ua', 'description_ua', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ua', 'name_en', 'name_ch', 'order_id', 'foods')
