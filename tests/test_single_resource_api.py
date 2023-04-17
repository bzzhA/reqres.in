import pytest
import requests

@pytest.mark.parametrize("color_id,expected_name,expected_year", [
    (1, "cerulean", 2000),
    (2, "fuchsia rose", 2001),
    (3, "true red", 2002)
])
def test_get_color_by_id(color_id, expected_name, expected_year):
    url = f"https://reqres.in/api/unknown/{color_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['name'] == expected_name
    assert data['year'] == expected_year

def test_get_invalid_color_id():
    url = "https://reqres.in/api/unknown/999"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {}

