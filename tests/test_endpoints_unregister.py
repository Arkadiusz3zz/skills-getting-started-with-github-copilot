from src.app import activities


def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Debate Team"
    email = "remove.me@mergington.edu"
    activities[activity_name]["participants"].append(email)
    endpoint = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]
