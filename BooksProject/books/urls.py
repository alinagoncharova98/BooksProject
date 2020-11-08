from django.urls import path
from .views import *


urlpatterns = [
    path('', BookListView.as_view(), name='list'),       # Shows all books
    path('add', BookAddView.as_view(), name='add'),      # Adds books
]
