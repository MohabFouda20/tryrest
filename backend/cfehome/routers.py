from rest_framework.routers import DefaultRouter

from product.viewset import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')

urlpatterns = router.urls