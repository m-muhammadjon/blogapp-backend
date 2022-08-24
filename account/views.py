from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from account.serializers import UserSerializer, UserUpdateSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@api_view(['POST'])
@permission_classes([IsAdminUser])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def user_login(request):
    user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
    print(request.data)
    print(user)
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


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_update(request):
    print(request.user)
    user = request.user
    serializer = UserUpdateSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
