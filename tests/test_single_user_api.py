import pytest
import requests

from pom.pages.users_page_api import UsersPage


class TestUsersPage:

    @pytest.fixture(scope="class")
    def users_page(self):
        return UsersPage()

    @pytest.mark.parametrize("page, expected_status", [(2, 200)])
    def test_get_single_user_status_code(self, page, expected_status, users_page):
        response = users_page.get_users(page)
        assert response.status_code == expected_status

    @pytest.fixture
    def user(self):
        response = requests.get("https://reqres.in/api/users/2")
        return response.json()["data"]

    def test_get_single_user_data(self, user):
        assert user["id"] == 2
        assert user["email"] == "janet.weaver@reqres.in"
        assert user["first_name"] == "Janet"
        assert user["last_name"] == "Weaver"
        assert user["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
