from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .models import Product, Filial, FilialPrice, Characteristic
from .serializers import CharacteristicSerializer, FilialPriceSerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # catalog/?filial=4
    def list(self, request):
        products = FilialPrice.objects.all()
        if request.GET.get("filial"):
            products = products.filter(filial=request.GET.get("filial"))

        ps = []
        if request.GET.get("characteristic"):
            ch = Characteristic.objects.filter(id=request.GET.get("characteristic")).first()
            if not ch:
                return Response({"message": "Characteristics not found!"}, status=status.HTTP_404_NOT_FOUND)
            for p in products:
                if ch in p.get_characteristics():
                    ps.append(p)
        else:
            ps = products

        paginator = PageNumberPagination()
        paginator.page_size = 5
        if request.GET.get('size'):
            paginator.page_size = request.GET.get('size')
        result_page = paginator.paginate_queryset(ps, request)
        serializer = FilialPriceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    # catalog/<product_id>/?filial=<id> or
    # catalog/<product_id>/price/?filial=<id>
    # Yokardaky urllerin ikisem shol bir zady soraya, ikisindede product bilen baha soralya, shon uchin ikisinem bir edip goyberdim
    def retrieve(self, request, pk=None):
        filial = None
        if request.GET.get("filial"):
            filial = Filial.objects.filter(id=request.GET.get("filial")).first()

        product = Product.objects.filter(id=pk).first()
        if not product:
            return Response({"message": "Product not found!"}, status=status.HTTP_404_NOT_FOUND)

        products = None
        if filial:
            products = FilialPrice.objects.filter(filial=filial, product=product)
        else:
            products = FilialPrice.objects.filter(product=product)

        paginator = PageNumberPagination()
        paginator.page_size = 5
        if request.GET.get('size'):
            paginator.page_size = request.GET.get('size')
        result_page = paginator.paginate_queryset(products, request)
        serializer = FilialPriceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    # Get product characteristics
    @action(methods=['get'], detail=True)
    def characteristics(self, request, pk=None):
        product = Product.objects.filter(id=pk).first()

        if not product:
            return Response({"message": "Product not found!"}, status=status.HTTP_404_NOT_FOUND)

        characteristics = product.characteristics.all()
        serializer = CharacteristicSerializer(characteristics, many=True)
        return Response(serializer.data)

    def create(self, request):
        if "name" not in request.data:
            return Response({"message": "Product name is required!"}, status=status.HTTP_404_NOT_FOUND)
        name = request.data["name"]
        product = Product()
        product.name = name
        product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
