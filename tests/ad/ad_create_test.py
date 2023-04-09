import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category):
    """
    Тест на создание одного объявления
    """
    data = {
        "author": user.username,
        "category": category.name,
        "name": "test_new_ad",
        "price": 600
    }

    expected_response = {
        "id": 1,
        "author": user.username,
        "category": category.name,
        "name": "test_new_ad",
        "price": 600,
        "description": None,
        "is_published": False,
        "image": None
    }

    response = client.post(
        "/ad/",
        data=data,
        content_type="application/json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response

