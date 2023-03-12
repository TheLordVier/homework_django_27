import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def main_view(request):
    """
    Представление (view) для обращения к корневому домену /
    """
    if request.method == 'GET':
        return JsonResponse({"status": "ОК"}, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    """
    Представление (view) для обращения ко всем категориям и создания новой категории
    """
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"]
        )

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    """
    Представление (view) для обращения к конкретной категории по id
    """
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    """
    Представление (view) для обращения ко всем объявлениям и создания нового объявления
    """
    def get(self, request):
        ads = Ad.objects.all()

        response = []

        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )

        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    """
    Представление (view) для обращения к конкретному объявлению по id
    """
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, safe=False, json_dumps_params={"ensure_ascii": False})
