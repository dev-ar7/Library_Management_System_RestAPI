from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, status


@api_view(['GET'])
def get_current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):

    permission_classes = (permissions.AllowAny)

    def post(self, request):
        if request.method == 'POST':
            user = request.data.get('user')
            if not user:
                return Response({'message' : 'No data found'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = UserSerializer(user = user)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Success'}, status=status.HTTP_200_OK)
            return Response({'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)