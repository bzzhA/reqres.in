import pytest
import requests

@pytest.mark.parametrize("page,per_page", [
    (1, 6),
    (2, 6),
    (1, 3)
])
def test_get_colors(page, per_page):
    url = f"https://reqres.in/api/unknown?page={page}&per_page={per_page}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == per_page
    for color in data:
        assert 'id' in color
        assert 'name' in color
        assert 'year' in color
        assert 'color' in color
        assert 'pantone_value' in color

