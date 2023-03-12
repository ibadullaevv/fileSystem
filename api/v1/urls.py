from django.urls import path, include

urlpatterns = [
    path('documents/', include('api.v1.documents.urls'))
]
