from rest_framework import routers
# from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register('doc', views.DocumentViewSet)
router.register('users', views.UserListDetailViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('users', views.UserListView.as_view())
# ]
