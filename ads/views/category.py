import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category


class CategoryListView(ListView):
    """
    Представление (view) для обращения ко всем категориям
    """
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = [{"id": category.id, "name": category.name} for category in self.object_list.order_by("name")]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


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
class CategoryCreateView(CreateView):
    """
    Представление (view) для создания новой категории
    """
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        new_category = Category.objects.create(name=data.get("name"))

        response = {
            "id": new_category.id,
            "name": new_category.name
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    """
    Представление (view) для обновления категории
    """
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        self.object.name = data["name"]

        self.object.save()

        response = {
            "id": self.object.id,
            "name": self.object.name
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    """
    Представление (view) для удаления категории
    """
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({"status": "Deleted"}, status=204)
