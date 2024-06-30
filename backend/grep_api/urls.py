from django.urls import path
from .views import *

urlpatterns = [
    path('grep/', run_grep, name='run grep')
]