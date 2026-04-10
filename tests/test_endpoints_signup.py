from src.app import activities


def test_signup_adds_participant_to_activity(client):
    # Arrange
    activity_name = "Soccer Team"
    email = "new.student@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup"
    assert email not in activities[activity_name]["participants"]

    # Act
    response = client.post(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert email in activities[activity_name]["participants"]
