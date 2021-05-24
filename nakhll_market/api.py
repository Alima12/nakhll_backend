from nakhll_market.models import (
    AmazingProduct, Product, Shop, Slider, Category
    )
from nakhll_market.serializers import (
    AmazingProductSerializer, ProductDetailSerializer,
    ProductSerializer, ShopSerializer,SliderSerializer,
    CategorySerializer
    )
from rest_framework import generics, routers, views, viewsets
from rest_framework import permissions, filters, mixins
from django.db.models import Q, F, Count
import random


class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SliderSerializer
    permission_classes = [permissions.AllowAny, ]
    search_fields = ('Location', )
    filter_backends = (filters.SearchFilter,)
    queryset = Slider.objects.filter(Publish=True)

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        categories = Category.objects\
            .filter(Publish = True, Available = True, FK_SubCategory = None)\
            .annotate(product_count = Count('ProductCategory'))\
            .filter(product_count__gt=5)
        categories_id = list(categories\
            .values_list('id', flat=True))
        categories = categories\
            .filter(pk__in=random.sample(categories_id, 12))
        return categories

class AmazingProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AmazingProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return AmazingProduct.objects.get_amazing_products()

class LastCreatedProductsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return Product.objects\
            .filter(Publish = True, Available = True, OldPrice = '0', Status__in = ['1', '2', '3'])\
                .order_by('-DateCreate')[:12]

class LastCreatedDiscountedProductsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return Product.objects\
            .filter(Publish = True, Available = True, Status__in = ['1', '2', '3'])\
            .exclude(OldPrice='0')\
            .order_by('-DateCreate')[:16]

class RandomShopsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        # Shop.objects\
        # .filter(Publish = True, Available = True)\
        # .annotate(product_count = Count('ShopProduct'))\
        # .filter(product_count__gt=1)\
        # .order_by('?')[:12]
        sql = '''
            SELECT 
                "nakhll_market_shop"."ID",
                "nakhll_market_shop"."FK_ShopManager_id",
                "nakhll_market_shop"."Title",
                "nakhll_market_shop"."Slug",
                "nakhll_market_shop"."Description",
                "nakhll_market_shop"."Image",
                "nakhll_market_shop"."NewImage",
                "nakhll_market_shop"."ColorCode",
                "nakhll_market_shop"."Bio",
                "nakhll_market_shop"."State",
                "nakhll_market_shop"."BigCity",
                "nakhll_market_shop"."City",
                "nakhll_market_shop"."Location",
                "nakhll_market_shop"."Point",
                "nakhll_market_shop"."Holidays",
                "nakhll_market_shop"."DateCreate",
                "nakhll_market_shop"."DateUpdate",
                "nakhll_market_shop"."Edite",
                "nakhll_market_shop"."Available",
                "nakhll_market_shop"."Publish",
                "nakhll_market_shop"."FK_User_id",
                "nakhll_market_shop"."CanselCount",
                "nakhll_market_shop"."CanselFirstDate",
                "nakhll_market_shop"."LimitCancellationDate",
                "nakhll_market_shop"."documents",
                COUNT("nakhll_market_product"."ID") AS "product_count" 
            FROM "nakhll_market_shop" 
            LEFT OUTER JOIN 
                "nakhll_market_product" ON ("nakhll_market_shop"."ID" = "nakhll_market_product"."FK_Shop_id") 
            WHERE ("nakhll_market_shop"."Available" AND "nakhll_market_shop"."Publish") 
            GROUP BY "nakhll_market_shop"."ID" HAVING COUNT("nakhll_market_product"."ID") > 1  
            ORDER BY RANDOM() 
            LIMIT 12
        '''
        return Shop.objects.raw(sql)

class RandomProductsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return Product.objects\
            .filter(
                Publish = True,
                Available = True,
                OldPrice = '0',
                Status__in = ['1', '2', '3']
                )\
            .order_by('?')[:16]

class MostDiscountPrecentageProductsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return Product.objects\
            .get_most_discount_precentage_available_product()\
            .order_by('?')[:15]

class MostSoldShopsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return Shop.objects.most_last_week_sale_shops()


class ProductDetailsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny, ]
    lookup_field = 'Slug'
    queryset = Product.objects.all()

class ProductsInSameFactorViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        id = self.kwargs.get('ID')
        try:
            product = Product.objects.get(ID=id)
            return Product.objects\
                .filter(Factor_Product__Factor_Products__FK_FactorPost__FK_Product=product)\
                .exclude(ID = product.ID)\
                .distinct()
        except:
            return None