from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db.models import Q
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']
        if len(password) < 8:
            raise ValidationError({'password': 'Password is too short'})

        user = User.objects.create(
            username=serializer.validated_data['username'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            )
        user.is_active = True
        user.set_password(password)
        user.save()

        return Response({'message': 'success'}, status=HTTP_201_CREATED)

    @action(methods=['POST'], detail=False)
    def login(self, request):
        if 'username' not in request.data:
            data = {'username': 'Username must be provided'}
            if 'password' not in request.data:
                data['password'] = ['Password must be provided']
            raise ValidationError(data)
        if 'password' not in request.data:
            raise ValidationError({'password': ['Password must be provided']})

        try:
            user = User.objects.get(username=request.data.get('username'))
        except User.DoesNotExist:
            raise NotFound({'message': 'User with provided credentials does not exist'})

        if not user.check_password(request.data.get('password')):
            raise AuthenticationFailed({'message': 'Incorrect password'})

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response

    @action(methods=['GET'], detail=False,
            permission_classes=[IsAuthenticated])
    def user(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data)

    @action(detail=True, methods=['POST'], url_path='change_username')
    def change_username(self, request, pk=None):
        if 'new_username' not in request.data:
            raise ValidationError({'username': 'Username must be provided'})

        username = request.data['new_username']
        user = User.objects.get(id=pk)
        user.username = username
        user.save()
        return Response({'status': 'username changed'})


