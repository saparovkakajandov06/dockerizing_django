from django.urls import path, include
from catalog.views_api import CatalogViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'catalog', CatalogViewSet, basename='Catalog')

urlpatterns = [
    path('users/', include('accounts.urls_api')),
]
print(router.urls)
urlpatterns += router.urls
