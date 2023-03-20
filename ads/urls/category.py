from django.urls import path

from ads.views.category import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path("", CategoryListView.as_view(), name="all_categories"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="detail_category"),
    path("create/", CategoryCreateView.as_view(), name="create_category"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="update_category"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete_category"),
]
