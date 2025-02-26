from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('documento2/', documento2, name='documento2'),
    path('logout/', logout_view, name='logout'),
]