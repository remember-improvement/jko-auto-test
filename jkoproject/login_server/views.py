# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_server.serailizers import (
    LoginRequiredSerializer,
    LoginLengthSerializer,
)
import json


@csrf_exempt
def login_view(request):
    correct_username = "correctuser"
    correct_auth = "Aa12345678"
    if request.method == "POST":
        try:
            request_body = request.body
            request_json = json.loads(request_body)

        except json.JSONDecodeError:
            response_data = {"Status": 400, "Message": "request body is required"}
            return JsonResponse(response_data, status=400)

        required_validation = LoginRequiredSerializer(data=request_json)
        length_validation = LoginLengthSerializer(data=request_json)
        if required_validation.is_valid():
            pass
        else:
            invalid_field = list(required_validation.errors)[0]
            response_data = {"Status": 400, "Message": f"{invalid_field} is required"}

            return JsonResponse(response_data, status=400)
        if length_validation.is_valid():
            pass
        else:
            invalid_field = list(length_validation.errors)[0]
            response_data = {
                "Status": 400,
                "Message": f"{invalid_field} length too long",
            }
            return JsonResponse(response_data, status=400)
        account = request_json["Account"]
        login_auth = request_json["LoginAuth"]

        if account == correct_username and login_auth == correct_auth:
            response_data = {"Status": 200, "Message": "Login successful"}
            return JsonResponse(response_data, status=200)

        elif account != correct_username or login_auth != correct_auth:
            response_data = {"Status": 401, "Message": "Login failed"}
            return JsonResponse(response_data, status=401)

    else:
        response_data = {"Status": 405, "Message": "Method should be POST"}
        return JsonResponse(response_data, status=405)
