import requests
import allure
import pytest


test_data = [
    (
        "Login Successful",
        {
            "Account": "correctuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        200,
        "Login successful",
    ),
    (
        "Login Failed with incorrect username",
        {
            "Account": "unkwownuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        401,
        "Login failed",
    ),
    (
        "Login Failed with incorrect loginAuth",
        {
            "Account": "correctuser",
            "LoginAuth": "0000",
            "DateTime": "2023-08-10T12:00:00",
        },
        401,
        "Login failed",
    ),
    (
        "Login Failed without account",
        {"LoginAuth": "0000", "DateTime": "2023-08-10T12:00:00"},
        400,
        "Account is required",
    ),
    (
        "Login Failed without loginAuth",
        {"Account": "currentuser", "DateTime": "2023-08-10T12:00:00"},
        400,
        "LoginAuth is required",
    ),
    (
        "Login Successful without DateTime",
        {"Account": "correctuser", "LoginAuth": "Aa12345678"},
        200,
        "Login successful",
    ),
    (
        "Login Successful with incorrect DateTime",
        {"Account": "correctuser", "LoginAuth": "Aa12345678", "DateTime": "123"},
        200,
        "Login successful",
    ),
    (
        "Login Failed with long account",
        {
            "Account": "currentuser1234567890",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        400,
        "Account length too long",
    ),
    (
        "Login Failed with long loginAuth",
        {
            "Account": "currentuser",
            "LoginAuth": "Aa12345678Aa12345678Aa123456787654321",
            "DateTime": "2023-08-10T12:00:00",
        },
        400,
        "LoginAuth length too long",
    ),
    (
        "Login Failed with long DateTime",
        {
            "Account": "currentuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00xx",
        },
        400,
        "DateTime length too long",
    ),
    ("Login Failed without body", None, 400, "request body is required"),
    (
        "Login Failed with invalid request method",
        {
            "Account": "correctuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        405,
        "Method should be POST",
    ),
]

API_URL = "http://127.0.0.1:8000/service/login"


@allure.feature("Login API Tests")
@pytest.mark.parametrize(
    "title, payload, status, message",
    test_data,
)
def test_login_api(title, payload, status, message):
    allure.dynamic.title(title)
    body = payload
    if title == "Login Failed with invalid request method":
        with allure.step("sending GET request"):
            response = requests.get(API_URL, json=body)
    else:
        with allure.step("sending POST request"):
            response = requests.post(API_URL, json=body)
    with allure.step("Verifying response status code and content"):
        res_json = response.json()
        assert response.status_code == status
        assert res_json["Status"] == status
        assert res_json["Message"] == message
