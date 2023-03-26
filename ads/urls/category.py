from rest_framework import routers

from ads.views.category import CategoryViewSet

router = routers.SimpleRouter()
router.register("", CategoryViewSet)

urlpatterns = router.urls
