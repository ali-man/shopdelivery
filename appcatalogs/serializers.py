from rest_framework import serializers

from appcatalogs.models import Category, Product, Brand, VolumeDesignation


class ParentCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parent = ParentCategorySerializer()

    class Meta:
        model = Category
        fields = ('name', 'parent')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', )


class VolumeDesignationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VolumeDesignation
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # read_only=True
    brand = BrandSerializer()
    volume_designation = VolumeDesignationSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'price_own', 'discount',
                  'price_discount', 'volume', 'volume_designation', 'category', 'brand')
