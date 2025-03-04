from django.urls import path
from .views import (
    UserListCreateView, UserDetailView, UserLoginView,
    PasswordResetRequestView, PasswordChangeView
)

urlpatterns = [
    path('usuarios/', UserListCreateView.as_view(), name='usuarios-list-create'),
    path('usuarios/<int:pk>/', UserDetailView.as_view(), name='usuarios-detail'),
    path('usuarios/login/', UserLoginView.as_view(), name='usuarios-login'),
    path('usuarios/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('usuarios/password-change/', PasswordChangeView.as_view(), name='password-change'),
]
