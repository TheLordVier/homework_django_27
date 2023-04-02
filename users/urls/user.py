from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.user import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView


urlpatterns = [
    path("", UserListView.as_view(), name="all_users"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail_user"),
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update_user"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete_user"),
    path('token/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="get_refresh_token"),
]
