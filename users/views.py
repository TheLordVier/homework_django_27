import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from homework_django import settings

from users.models import User, Location


class UserListView(ListView):
    """
    Представление (view) для обращения ко всем пользователям
    """
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        response = {"items": [{
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": [location.name for location in user.location.all()],
            "total_ads": user.total_ads,
        } for user in self.object_list.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True)))],
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages, }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class UserDetailView(DetailView):
    """
    Представление (view) для обращения к конкретному пользователю по id
    """
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        response = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "location": [location.name for location in user.location.all()],
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    """
    Представление (view) для создания пользователя
    """
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        locations = data.pop("location")
        new_user = User.objects.create(**data)

        for location_name in locations:
            location, _ = Location.objects.get_or_create(name=location_name)
            new_user.location.add(location)

        return JsonResponse({
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "username": new_user.username,
            "role": new_user.role,
            "age": new_user.age,
            "location": [location.name for location in new_user.location.all()],
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    """
    Представление (view) для обновления пользователя
    """
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if "first_name" in data:
            self.object.first_name = data.get("first_name")
        if "last_name" in data:
            self.object.last_name = data.get("last_name")
        if "username" in data:
            self.object.username = data.get("username")
        if "role" in data:
            self.object.role = data.get("role")
        if "age" in data:
            self.object.age = data.get("age")
        if "location" in data:
            self.object.location.clear()
            for location_name in data.get("location"):
                location, _ = Location.objects.get_or_create(name=location_name)
                self.object.location.add(location)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "location": [location.name for location in self.object.location.all()],
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    """
    Представление (view) для удаления пользователя
    """
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({"status": "Deleted"}, status=204)
