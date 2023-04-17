import pytest
from pom.pages.users_page_api import UsersPage
import requests


class TestUsers:

    @pytest.fixture(scope="session")
    def users_page(self):
        return UsersPage()

    def get_users(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        data = response.json()
        return data
    @pytest.mark.parametrize("page, expected_status", [(1, 200), (2, 200), (3, 200)])
    def test_get_users_status(self, page, expected_status, users_page):
        response = users_page.get_users(page)
        assert response.status_code == expected_status

    @pytest.mark.parametrize("page, expected_total", [(1, 12), (2, 12), (3, 12)])
    def test_get_users_total(self, page, expected_total, users_page):
        response = users_page.get_users(page)
        assert response.json()["total"] == expected_total

    @pytest.mark.parametrize("page, expected_users", [(1, ["George", "Janet", "Emma", "Eve", "Charles", "Tracey"]),
                                                          (2, ["Michael", "Lindsay", "Tobias", "Byron", "George",
                                                               "Rachel"])])
    def test_get_users_names(self, page, expected_users, users_page):
        response = users_page.get_users(page)
        users = [user["first_name"] for user in response.json()["data"]]
        assert users == expected_users
