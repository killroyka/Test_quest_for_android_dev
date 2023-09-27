from django.urls import path

from .views import RouteListView, RouteView

urlpatterns = [
    path('route/', RouteListView.as_view()),
    path('route/<int:pk>/', RouteView.as_view()),
]
