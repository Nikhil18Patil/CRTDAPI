from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import Apiregister, PasskeyViewSet, JobcodeViewSet

register_router = SimpleRouter()
register_router.register(r'register', Apiregister, basename='register')

Passkey_router = SimpleRouter()
Passkey_router.register(r'passkey',PasskeyViewSet, basename='passkey')


jobcode_router = SimpleRouter()
jobcode_router.register(r'jobcode',JobcodeViewSet, basename='jobcode')

urlpatterns = [
    path('api/',include(register_router.urls) ),
    path('api/', include(Passkey_router.urls)),
    path('api/',include(jobcode_router.urls))
]