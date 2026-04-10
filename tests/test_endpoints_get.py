from src.app import activities


def test_get_activities_returns_dictionary_with_data(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload
    assert set(payload.keys()) == set(activities.keys())


def test_root_redirects_to_static_index(client):
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint, follow_redirects=False)

    # Assert
    assert response.status_code in {302, 307}
    assert response.headers["location"] == "/static/index.html"
