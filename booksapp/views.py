from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from booksapp.models import Books
from booksapp.serializers import BookSerializer


# Create your views here.

class BookView(APIView,UpdateModelMixin,DestroyModelMixin):
  def get(self,request,id=None):
    query_set = None
    response_serializer = None
    if id:
      try:
        queryset = Books.objects.get(id=id)
      except Books.DoesNotExist:
        return Response({'errors': 'This todo item does not exist.'}, status=400)

      response_serializer = BookSerializer(queryset)
    else:
      queryset = Books.objects.all()
      response_serializer = BookSerializer(queryset, many=True)
    return Response({"status": "success", "data":response_serializer.data}, status=status.HTTP_200_OK)

  def post(self, request):
    request_serializer = BookSerializer(data=request.data)

    if request_serializer.is_valid():
      book = request_serializer.save()
      response_serializer = BookSerializer(book)
      return Response(response_serializer.data, status=201)
    return Response(request_serializer.errors, status=400)

  def put(self, request, id=None):
    try:
      book = Books.objects.get(id=id)
    except Books.DoesNotExist:
      return Response({'errors': 'This book does not exist.'}, status=400)
    request_serializer = BookSerializer(book, data=request.data)

    if request_serializer.is_valid():
      book = request_serializer.save()
      response_serializer = BookSerializer(book)
      return Response(response_serializer.data, status=200)
    return Response(request_serializer.errors, status=400)

  def delete(self, request, id=None):
    try:
      book = Books.objects.get(id=id)
    except Books.DoesNotExist:
      return Response({'errors': 'This book does not exist.'}, status=400)
    book.delete()
    return Response(status=204)