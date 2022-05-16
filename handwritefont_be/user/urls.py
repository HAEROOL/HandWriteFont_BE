"""handwritefont_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import HWFUserDetail,EmailUniqueCheck, NickNameUniqueCheck
from main.views import Font
# from .views import HWFUserView,HWFUserListView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/',include('dj_rest_auth.registration.urls')),
    path('registration/email-check/',EmailUniqueCheck.as_view()),
    path('registration/nickname-check/',NickNameUniqueCheck.as_view()),
    # path('list/', HWFUserListView.as_view()),
    path('<str:pk>/', HWFUserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

#  path('', include('dj_rest_auth.urls')),
# http://localhost:8000/users/password/reset/
# http://localhost:8000/users/password/reset/confirm/
# http://localhost:8000/users/login/
# http://localhost:8000/users/logout/
# http://localhost:8000/users/user/
# http://localhost:8000/users/password/change/
# http://localhost:8000/users/token/verify/
# http://localhost:8000/users/token/refresh/