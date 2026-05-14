from django import views
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from  rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from book.models import *
from .serlizer import *

class BookUpdate(UpdateAPIView):
    queryset = Book.objects.filter(is_active=True)
    lookup_field = 'id'
    serializer_class = BookSerlizer

    # def perform_update(self, serializer):
    #     pass







class Createbook(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self,request,formate=None):
        #book data json
        bookser_obj=BookSerlizer(data=request.data)
        #validate
        if bookser_obj.is_valid():
            #insert
            bookser_obj.save()
            return Response(
                data={
                    'msg':'book created',
                    'data':bookser_obj.data  }
                ,status=status.HTTP_201_CREATED
            )
        return Response(bookser_obj.errors,status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def listbook(request,id=None):
    if(id):
        # read book from db
        book = Book.objects.select_related('Catagory').get(pk=id)
        # serlizer
        bookserlized = BookSerlizer(book)
        return Response(data=bookserlized.data, status=status.HTTP_200_OK)

    else:
        #read book from db
        books=Book.objects.select_related('Catagory').filter(is_active=True)
        #serlizer
        bookserlized=BookSerlizer(books,many=True)
        #return response
        return Response(data=bookserlized.data,status=status.HTTP_200_OK)




def json(request):
    # print(Book.objects.all())
    books=Book.objects.values('id','title')
    # print(Book.objects.values('id','title'))
    return JsonResponse(list(books),safe=False)