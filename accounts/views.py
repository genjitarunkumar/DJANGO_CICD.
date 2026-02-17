from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from .models import UserCredential

class UserCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredential
        fields = ['id', 'username', 'password', 'created_at']

@api_view(['GET'])
def hello_world(request):
    return Response({
        "message": "HELLO WORLD"
    })

class UserCredentialViewSet(viewsets.ModelViewSet):
    queryset = UserCredential.objects.all()
    serializer_class = UserCredentialSerializer
