from django.urls import path
from . import views

urlpatterns = [
    path('api/get', views.PersonViewSet.as_view({'get': 'list'}), name='get'),
    path('api/get/<int:pk>', views.PersonViewSet.as_view({'get': 'retrieve'}), name='get-by-id'),
    path('api/set', views.PersonViewSet.as_view({'post':'create'}), name='set'),
]