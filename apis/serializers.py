from rest_framework import serializers
from home import models


class HomeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'home_title',
            'home_image',
            'home_url'
        )
        model = models.HomeNews

class SportNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'sports_title',
            'sports_image',
            'sports_url'
        )
        model = models.SportsNews

class BusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'business_title',
            'business_image',
            'business_url'
        )
        model = models.BusinessNews
    
class WorldNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'world_title',
            'world_image',
            'world_url'
        )
        model = models.WorldNews

class PoliticsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'politics_title',
            'politics_image',
            'politics_url'
        )
        model = models.PoliticsNews

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'subject',
            'message'
        )
        model = models.Contact

