from django.urls import path,include
from book.views import *
urlpatterns = [
    # path('API/',include('book.api.urls') ),

    path('', BookList.as_view(), name='Booklist'),
    path('<int:id>/', getbookbyid, name='Book_get'),

    path('Update/<int:id>/',bookupdate,name='Book_update'),
    path('HDelete/<int:id>/',Hardbookdelete,name='HBook_delete'),
    path('SDelete/<int:id>/',softbookdelete,name='sBook_delete'),
    path('New/',BookNew.as_view(),name='Book_add'),

    path('<str:name>/', getbookbyname, name='Book_get_name'),
    ]