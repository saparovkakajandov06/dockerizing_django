from rest_framework import serializers
from .models import Product, Filial, Characteristic, FilialPrice


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        return Product(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance


class FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filial
        fields = "__all__"

    def create(self, validated_data):
        return Filial(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.region = validated_data.get('region', instance.region)
        return instance


class CharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic
        fields = ["id", "name", "parent"]

    def create(self, validated_data):
        return Characteristic(**validated_data)

    def update(self, instance, validated_data):
        instance.parent = validated_data.get('parent', instance.parent)
        instance.name = validated_data.get('name', instance.name)
        instance.product = validated_data.get('product', instance.product)
        return instance


class FilialPriceSerializer(serializers.ModelSerializer):
    product_obj = serializers.SerializerMethodField()
    filial_obj = serializers.SerializerMethodField()

    def get_product_obj(self, obj):
        product = obj.product
        serializer = ProductSerializer(product, many=False)
        return serializer.data

    def get_filial_obj(self, obj):
        filial = obj.filial
        serializer = FilialSerializer(filial, many=False)
        return serializer.data

    class Meta:
        model = FilialPrice
        fields = [
            "id",
            "price",
            "product_obj",
            "filial_obj"
        ]

    def create(self, validated_data):
        return Characteristic(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.filial = validated_data.get('filial', instance.filial)
        instance.price = validated_data.get('price', instance.price)
        return instance
