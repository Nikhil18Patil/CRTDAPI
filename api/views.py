
from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, Passkey, JobCode
from .serializers import registerserializer, Passkeyserializer, JobcodeSerializer
from rest_framework.response import Response
from rest_framework import status 

class Apiregister(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = registerserializer


    def create(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      register = serializer.save()

      success_message = 'Successfully created register'
      return Response(
        data={'success': success_message},
        status=status.HTTP_201_CREATED,
      )


class PasskeyViewSet(viewsets.ModelViewSet):
    queryset = Passkey.objects.all()
    serializer_class = Passkeyserializer

    def create(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      register = serializer.save()

      success_message = 'Successfully created register'
      return Response(
        data={'success': success_message},
        status=status.HTTP_201_CREATED,
      )
    
# Create your views here.


class JobcodeViewSet(viewsets.ModelViewSet):
    queryset = JobCode.objects.all()
    serializer_class = JobcodeSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      register = serializer.save()

      success_message = 'Successfully created register'
      return Response(
        data={'success': success_message},
        status=status.HTTP_201_CREATED,
      )

# Create your views here.
