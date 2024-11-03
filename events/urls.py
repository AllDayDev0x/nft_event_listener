from django.urls import path
from . import views

urlpatterns = [
    path('transfer-history/<str:token_id>/', views.transfer_history, name='transfer_history'),
]