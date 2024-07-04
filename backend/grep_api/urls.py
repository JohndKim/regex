from django.urls import path
from .views import *

urlpatterns = [
    path('grep/', run_grep, name='run grep'),
    path('upload/', run_upload, name='upload')
]