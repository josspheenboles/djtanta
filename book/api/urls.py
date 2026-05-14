from django.urls import path
from .views import *
urlpatterns=[

    path('json/',json),
    path('List/',listbook),
    path('List/<int:id>/',listbook),
    path('Add/',Createbook.as_view()),
    path('Update/<int:id>',BookUpdate.as_view())

]