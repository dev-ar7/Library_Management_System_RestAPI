from django.urls import path
from .views import *


urlpatterns = [
    path('current_user/', get_current_user),
    path('user/create', CreateUserView().as_view())
]