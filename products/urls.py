from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'products', views.ProductList)

urlpatterns = router.urls