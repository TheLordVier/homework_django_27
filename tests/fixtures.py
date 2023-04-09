import pytest


@pytest.fixture
@pytest.mark.django_db
def user_access_token(client, django_user_model):
    """
    Фикстура получения access token
    """
    username = "test_user"
    password = "test_password"
    django_user_model.objects.create_user(username=username, password=password, role="admin")
    response = client.post("/user/token/", data={"username": username, "password": password}, format="json")
    return response.data.get("access")


@pytest.fixture
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    """
    Фикстура получения user и access token
    """
    username = "test_user"
    password = "test_password"
    test_user = django_user_model.objects.create_user(username=username, password=password, role="admin")
    response = client.post("/user/token/", data={"username": username, "password": password}, format="json")
    return test_user, response.data.get("access")
