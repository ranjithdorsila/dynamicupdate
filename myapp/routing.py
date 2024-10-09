from django.urls import path
from .consumers import ResultConsumer

websocket_urlpatterns = [
    path('ws/generate/', ResultConsumer.as_asgi()),
]
