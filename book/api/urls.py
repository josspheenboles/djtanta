from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter,DefaultRouter

drouter=DefaultRouter()
drouter.register(r'VS',Bookviewset,basename='VS')
urlpatterns=[
    path('',include(drouter.urls)),
    path('json/',json),
    path('List/',listbook),
    path('List/<int:id>/',listbook),
    path('Add/',Createbook.as_view()),
    path('Update/<int:id>',BookUpdate.as_view())

]