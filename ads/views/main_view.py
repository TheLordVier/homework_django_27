from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def main_view(request):
    """
    Представление (view) для обращения к корневому домену /
    """
    if request.method == 'GET':
        return JsonResponse({"status": "ОК"}, safe=False, json_dumps_params={"ensure_ascii": False})
