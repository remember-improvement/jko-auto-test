from rest_framework import serializers


class LoginRequiredSerializer(serializers.Serializer):
    Account = serializers.CharField(required=True)
    LoginAuth = serializers.CharField(required=True)
    DateTime = serializers.CharField(required=False)


class LoginLengthSerializer(serializers.Serializer):
    Account = serializers.CharField(max_length=20)
    LoginAuth = serializers.CharField(max_length=36)
    DateTime = serializers.CharField(max_length=20, required=False)


class LoginTypeSerializer(serializers.Serializer):
    Account = serializers.CharField(required=True)
    LoginAuth = serializers.CharField(required=True)
    DateTime = serializers.CharField(required=False)

    def validate_Account(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Account must be a string.")
        return value

    def validate_LoginAuth(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("LoginAuth must be a string.")
        return value

    def validate_DateTime(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("DateTime must be a string.")
        return value
