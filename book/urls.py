from django.urls import path
from book.views import *
urlpatterns = [
    path('', listbook, name='Booklist'),
    path('<int:id>/', getbookbyid, name='Book_get'),

    path('Update/<int:id>/',bookupdate,name='Book_update'),
    path('Delete/<int:id>/',bookdelete,name='Book_delete'),
    path('New/',newbook,name='Book_add'),

    path('<str:name>/', getbookbyname, name='Book_get_name'),
    ]