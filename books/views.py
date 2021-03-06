from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
