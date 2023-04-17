import requests

class UsersPage:

    def __init__(self):
        self.base_url = "https://reqres.in/api"

    def get_users(self, page):
        url = f"{self.base_url}/users?page={page}"
        response = requests.get(url)
        return response

    def get_user(self, page):
        url = f"{self.base_url}/users/{page}"
        response = requests.get(url)
        return response