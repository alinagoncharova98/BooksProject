from rest_framework import generics
from .models import Book
from .serializers import *


class BookAddView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookDetailSerializer
    # queryset = Book.objects.all()
    queryset = Book.objects.select_related('owner')
    # template_name = 'books/base.html'



