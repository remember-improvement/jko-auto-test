from rest_framework import serializers


class LoginRequiredSerializer(serializers.Serializer):
    Account = serializers.CharField(required=True)
    LoginAuth = serializers.CharField(required=True)
    DateTime = serializers.CharField(required=False)


class LoginLengthSerializer(serializers.Serializer):
    Account = serializers.CharField(max_length=20)
    LoginAuth = serializers.CharField(max_length=36)
    DateTime = serializers.CharField(max_length=20, required=False)
