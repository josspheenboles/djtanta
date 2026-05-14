from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

drouter=DefaultRouter()
drouter.register(r'VS',Bookviewset,basename='VS')
urlpatterns=[
    path('',include(drouter.urls)),
    path('json/',json),
    path('List/',listbook),
    path('List/<int:id>/',listbook),
    path('Add/',Createbook.as_view()),
    path('Update/<int:id>',BookUpdate.as_view()),

    #jwt
    # Login: Returns Access and Refresh tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh: Returns a new Access token using the Refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]