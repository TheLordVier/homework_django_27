import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad, Category
from homework_django import settings
from users.models import User


class AdListView(ListView):
    """
    Представление (view) для обращения ко всем объявлениям
    """
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author").order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        response = {"items": [{
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None,
        } for ad in page_obj],
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages, }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    """
    Представление (view) для обращения к конкретному объявлению по id
    """
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None,
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    """
    Представление (view) для создания объявления
    """
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "category", "image"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        author = get_object_or_404(User, pk=data.pop("author_id"))

        new_ad = Ad.objects.create(
            name=data["name"],
            author=author,
            price=data["price"],
            description=data["description"],
            is_published=data["is_published"],
            category_id=data['category_id'],
        )

        response = {
            "id": new_ad.id,
            "name": new_ad.name,
            "author_id": new_ad.author_id,
            "author": new_ad.author.first_name,
            "price": new_ad.price,
            "description": new_ad.description,
            "is_published": new_ad.is_published,
            "category_id": new_ad.category_id,
            "image": new_ad.image.url if new_ad.image else None,
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    """
    Представление (view) для обновления объявления
    """
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "category", "image"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if "name" in data:
            self.object.name = data.get("name")
        if "author_id" in data:
            author = get_object_or_404(User, pk=data.pop("author_id"))
            self.object.author_id = author
        if "price" in data:
            self.object.price = data.get("price")
        if "description" in data:
            self.object.price = data.get("description")
        if "is_published" in data:
            self.object.price = data.get("is_published")
        if "category_id" in data:
            category = get_object_or_404(Category, pk=data.pop("category_id"))
            self.object.category_id = category
        if "image" in data:
            self.object.price = data.get("image")

        self.object.save()

        response = {
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None,
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    """
    Представление (view) для удаления объявления
    """
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({"status": "Deleted"}, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class AdUpLoadImageView(UpdateView):
    """
    Представление (view) для загрузки картинок к объявлению
    """
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "category", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        response = {
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None,
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
