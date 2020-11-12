from django.views.generic import ListView, TemplateView, CreateView
from .models import Book
from .forms import *


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.select_related('owner')
        return context


class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookForm


# Another variant of creating django views

# from django.shortcuts import render, redirect
# from django.views import generic
# from .models import Book
# from .forms import *
#
#
# def book_list(request):
#     books = Book.objects.select_related('owner')
#     return render(request, 'book_list.html', {'title': 'Home View', 'books': books})
#
# def add_book(request):
#     error = ''
#
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('')
#
#         else:
#             error = 'Invalid format'
#
#     form = BookForm()
#     context = {
#         'form': form,
#         'error': error
#
#     }
#     return render(request, 'add_book.html', context)




