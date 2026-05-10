from django.urls import path

from .views import (
    home,
    RouteAPIView
)


urlpatterns = [

    path(
        '',
        home
    ),

    path(
        'route/',
        RouteAPIView.as_view()
    ),
]