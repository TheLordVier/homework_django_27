from django.urls import path

from ads.views.ad import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdUpLoadImageView

urlpatterns = [
    path("", AdListView.as_view(), name="all_ads"),
    path("<int:pk>/", AdDetailView.as_view(), name="detail_ad"),
    path("create/", AdCreateView.as_view(), name="create_ad"),
    path("<int:pk>/update/", AdUpdateView.as_view(), name="update_ad"),
    path("<int:pk>/delete/", AdDeleteView.as_view(), name="delete_ad"),
    path("<int:pk>/upload_image/", AdUpLoadImageView.as_view(), name="upload_image"),
]
