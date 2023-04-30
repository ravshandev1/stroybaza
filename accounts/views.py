import random
from rest_framework import generics, status, authentication, permissions, response
from rest_framework.authtoken.models import Token
from .utils import verify
from accounts.serializers import LoginSerializer, VerifySerializer, UserSerializer, UserCardSerializer
from accounts.models import Account, VerifyPhone, UserCard


class UserCardAPI(generics.CreateAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        qs = self.queryset.filter(user_id=self.request.user.id).all()
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)


class UserCardRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        phone = request.data['phone']
        kod = str(random.randint(1000, 10000))
        if len(phone) == 13:
            verify(phone, kod)
            v = VerifyPhone.objects.create(phone=phone, code=kod)
            v.save()
        return response.Response({'message': 'Please verify phone'}, status=status.HTTP_200_OK)


class VerifyPhoneAPIView(generics.GenericAPIView):
    serializer_class = VerifySerializer

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        code = request.data.get('code')
        verify = VerifyPhone.objects.filter(phone=phone, code=code).first()
        print(verify)
        if verify:
            try:
                user = Account.objects.filter(phone=phone).first()
            except:
                user = Account.objects.create_user(phone=phone, password='12345678')
            print(user)
            verify.delete()
            user.is_verified = True
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': "Phone number is verified",
                'token': str(token.key),
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        else:
            return response.Response({"message": "Invalid phone or code"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            user = self.request.user
            user.is_verified = False
            user.save()
            return Response({
                "message": "Logout Success"
            }, status=status.HTTP_200_OK)
        except:
            return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class MyAccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Account.objects.all()
