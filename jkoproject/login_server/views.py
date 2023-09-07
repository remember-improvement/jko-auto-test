# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_server.serailizers import LoginRequiredSerializer, LoginLengthSerializer
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
            response_data = {"Status": "ErrorCode_05", "Message": "XXX_05"}
            return JsonResponse(response_data, status=400)

        required_validation = LoginRequiredSerializer(data=request_json)
        length_validation = LoginLengthSerializer(data=request_json)
        if required_validation.is_valid():
            pass
        else:
            response_data = {"Status": "ErrorCode_01", "Message": "XXX_01"}

            return JsonResponse(response_data, status=400)
        if length_validation.is_valid():
            pass
        else:
            print(length_validation.errors)
            response_data = {"Status": "ErrorCode_02", "Message": "XXX_02"}
            return JsonResponse(response_data, status=400)
        account = request_json["Account"]
        login_auth = request_json["LoginAuth"]

        if account == correct_username and login_auth == correct_auth:
            response_data = {"Status": "Success", "Message": "Login successful"}
            return JsonResponse(response_data, status=200)

        elif account != correct_username or login_auth != correct_auth:
            response_data = {"Status": "ErrorCode_03", "Message": "XXX_03"}
            return JsonResponse(response_data, status=401)

    else:
        response_data = {"Status": "ErrorCode_04", "Message": "XXX_04"}
        return JsonResponse(response_data, status=405)
