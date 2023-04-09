import pytest
from rest_framework import status

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    """
    Тест на выдачу списка объявлений (без фильтров)
    """
    ad_list = AdFactory.create_batch(3)

    expected_response = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }

    response = client.get("/ad/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response

