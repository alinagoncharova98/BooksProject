from django.urls import path
from .views import *


urlpatterns = [
    path('', BookListView.as_view(), name='list'),      # Shows all books
    path('add', AddBookView.as_view(), name='add'),      # Adds books
    # path('add', add_book, name='add'),      # Adds books
]
