from rest_framework.routers import DefaultRouter
from app_inventario.api.views import ProductoViewSet

router= DefaultRouter()
router.register("Productos", ProductoViewSet, basename="producto")
urlpatterns = router.urls
