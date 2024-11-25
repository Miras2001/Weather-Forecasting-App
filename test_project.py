import pytest
from project import get_weather, display_weather

def test_get_weather(mocker):
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {
        "name": "TestCity",
        "main": {"temp": 25},
        "weather": [{"description": "clear sky"}],
    }
    result = get_weather("TestCity", "weather")
    assert result["name"] == "TestCity"
    assert result["main"]["temp"] == 25
    assert result["weather"][0]["description"] == "clear sky"

def test_display_weather(capfd):
    current_weather = {
        "name": "TestCity",
        "main": {"temp": 25},
        "weather": [{"description": "clear sky"}],
    }
    forecast = {
        "list": [
            {"dt_txt": "2024-11-24 12:00:00", "main": {"temp": 20}, "weather": [{"description": "rain"}]},
            {"dt_txt": "2024-11-25 12:00:00", "main": {"temp": 22}, "weather": [{"description": "cloudy"}]},
        ]
    }
    display_weather(current_weather, forecast)
    captured = capfd.readouterr()
    assert "TestCity" in captured.out
    assert "25°C" in captured.out
    assert "rain" in captured.out
