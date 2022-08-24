from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from account.serializers import UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@api_view(['POST'])
@permission_classes([IsAdminUser])
def user_login(request):
    user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
    status = 'error'
    token = ''
    if user is not None:
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        status = 'ok'
    res = {

        'status': status,
        'token': token
    }
    return Response(res)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request):
    try:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    except:
        return Response({'status': 'error'})
