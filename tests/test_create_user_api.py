import pytest
import requests

@pytest.mark.parametrize("name, job", [
    ("morpheus", "leader"),
    ("neo", "the one"),
    ("trinity", "hacker")
])
def test_create_user(name, job):
    url = "https://reqres.in/api/users"
    data = {"name": name, "job": job}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert 'id' in response.json()
    assert 'createdAt' in response.json()

