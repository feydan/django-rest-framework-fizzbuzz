from fizzbuzz.models import FizzBuzz
from fizzbuzz.serializers import FizzBuzzSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class FizzBuzzList(generics.ListCreateAPIView):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    def post(self, request, format=None):
        if request.content_type != 'application/json':
            return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        if 'HTTP_USER_AGENT' in request.META:
            request.data['useragent'] = request.META['HTTP_USER_AGENT'];
        serializer = FizzBuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FizzBuzzDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    def put(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)