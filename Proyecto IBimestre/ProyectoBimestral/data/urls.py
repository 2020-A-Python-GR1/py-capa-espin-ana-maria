from django.urls import path
from .views import chart_select_view

app_name = 'data'

urlpatterns = [
    path('',chart_select_view, name='main_products-view'),
]
