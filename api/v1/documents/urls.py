from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('doc', views.DocumentViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', views.AdminFileUploadView.as_view(),)
]