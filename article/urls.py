from rest_framework import routers
from .views import ArticleViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'category', CategoryViewSet)
urlpatterns = router.urls
