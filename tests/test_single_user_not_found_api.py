import pytest
import requests

@pytest.mark.parametrize("user_id,expected_status_code", [
    (2, 200),
    (23, 404),
    (100, 404)
])
def test_get_user(user_id, expected_status_code):
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        user_data = response.json()['data']
        assert user_data['id'] == user_id
    else:
        assert response.json() == {}
