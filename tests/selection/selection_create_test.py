import pytest
from rest_framework import status

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_with_access_token):
    """
    Тест на создание подборки
    """
    user, access_token = user_with_access_token
    ad_list = AdFactory.create_batch(6)
    data = {
        "name": "Compilation_test",
        "items": [ad.pk for ad in ad_list[1:6]]
    }

    expected_response = {
        "id": 1,
        "owner": user.username,
        "name": "Compilation_test",
        "items": [ad.pk for ad in ad_list[1:6]]
    }

    response = client.post(
        "/selection/",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {access_token}"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response
