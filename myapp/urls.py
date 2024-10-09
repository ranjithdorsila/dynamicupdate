
from django.shortcuts import render
from django.urls import path
from .views import process_input, output_page

urlpatterns = [
    path('', lambda request: render(request, 'myapp/input.html')),
    path('process-input/', process_input, name='process_input'),
    path('output/<str:input_id>/', output_page, name='output'),
]

