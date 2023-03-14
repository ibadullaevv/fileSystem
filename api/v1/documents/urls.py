from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('doc', views.DocumentViewSet)

urlpatterns = router.urls
