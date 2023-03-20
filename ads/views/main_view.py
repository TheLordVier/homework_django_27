from django.http import JsonResponse


def main_view(request):
    """
    Представление (view) для обращения к корневому домену /
    """
    if request.method == 'GET':
        return JsonResponse({"status": "ОК"}, safe=False, json_dumps_params={"ensure_ascii": False})
