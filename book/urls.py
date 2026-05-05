from django.urls import path
from book.views import *
urlpatterns = [
    path('', listbook, name='Booklist'),
    path('<int:id>/', getbookbyid, name='Book_get'),

    path('Update/<int:id>/',bookupdate,name='Book_update'),
    path('HDelete/<int:id>/',Hardbookdelete,name='HBook_delete'),
    path('SDelete/<int:id>/',softbookdelete,name='DBook_delete'),
    path('New/',newbook,name='Book_add'),

    path('<str:name>/', getbookbyname, name='Book_get_name'),
    ]