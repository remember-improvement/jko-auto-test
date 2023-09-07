import requests
import allure
import pytest


API_URL = "http://127.0.0.1:8000/service/login"
test_data = [
    (
        "Login Successful",
        {
            "Account": "correctuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        "Success",
        "Login successful",
        200,
    ),
    (
        "Login Failed with incorrect username",
        {
            "Account": "unkwownuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        "ErrorCode_03",
        "XXX_03",
        401,
    ),
    (
        "Login Failed with incorrect loginAuth",
        {
            "Account": "correctuser",
            "LoginAuth": "0000",
            "DateTime": "2023-08-10T12:00:00",
        },
        "ErrorCode_03",
        "XXX_03",
        401,
    ),
    (
        "Login Failed without username",
        {"LoginAuth": "0000", "DateTime": "2023-08-10T12:00:00"},
        "ErrorCode_01",
        "XXX_01",
        400,
    ),
    (
        "Login Failed without loginAuth",
        {"Account": "currentuser", "DateTime": "2023-08-10T12:00:00"},
        "ErrorCode_01",
        "XXX_01",
        400,
    ),
    (
        "Login Successful without DateTime",
        {"Account": "correctuser", "LoginAuth": "Aa12345678"},
        "Success",
        "Login successful",
        200,
    ),
    (
        "Login Successful with incorrect DateTime",
        {"Account": "correctuser", "LoginAuth": "Aa12345678", "DateTime": "123"},
        "Success",
        "Login successful",
        200,
    ),
    (
        "Login Failed with long username",
        {
            "Account": "currentuser1234567890",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        "ErrorCode_02",
        "XXX_02",
        400,
    ),
    (
        "Login Failed with long loginAuth",
        {
            "Account": "currentuser",
            "LoginAuth": "Aa12345678Aa12345678Aa123456787654321",
            "DateTime": "2023-08-10T12:00:00",
        },
        "ErrorCode_02",
        "XXX_02",
        400,
    ),
    (
        "Login Failed with long DateTime",
        {
            "Account": "currentuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00xx",
        },
        "ErrorCode_02",
        "XXX_02",
        400,
    ),
    (
        "Login Failed without body",
        None,
        "ErrorCode_05",
        "XXX_05",
        400,
    ),
    (
        "Login Failed with invalid request method",
        {
            "Account": "correctuser",
            "LoginAuth": "Aa12345678",
            "DateTime": "2023-08-10T12:00:00",
        },
        "ErrorCode_04",
        "XXX_04",
        405,
    ),
]


@allure.feature("Login API Tests")
@pytest.mark.parametrize(
    "title, payload, status, message, status_code",
    test_data,
)
def test_login_api(title, payload, status, message, status_code):
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
        assert response.status_code == status_code
        assert res_json["Status"] == status
        assert res_json["Message"] == message
