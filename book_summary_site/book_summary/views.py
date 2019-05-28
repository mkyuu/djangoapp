from django.shortcuts import get_object_or_404,redirect
from django.views import generic
from .forms import BookCreateForm,CommentCreateForm
from .models import BigCategory,Category,Author,Publisher,Comment,Book
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

app_name = 'book_summary'

class IndexView(generic.TemplateView):
    template_name = 'book_summary/index.html'


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_summary/book_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Book.objects.order_by('-published_date')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(summary__icontains=keyword)
                )
        return queryset
    

class BookAddView(LoginRequiredMixin,generic.CreateView):
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('book_summary:book_list')
    template_name = 'book_summary/book_form.html'

class BookUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book_summary/book_form.html'

    def get_success_url(self):
        return redirect('book_summary:book_detail',kwargs={'pk':self.kwargs['pk']}) 
        #　pkを取得して元のdetailに遷移

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book
    template_name = 'book_summary/book_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm
        return context

class BookDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Book
    template_name = 'book_summary/book_delete.html'
    success_url = reverse_lazy('book_summary:book_list')

class CommentView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'book_summary/book_detail.html'

    def form_valid(self,form):
        book_pk = self.kwargs['book_pk']
        comment = form.save(commit=False)
        comment.book = get_object_or_404(Book,pk=book_pk)
        comment = form.save()
        return redirect('book_summary:book_detail',pk=book_pk)

class CommentDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Comment
    template_name = 'book_summary/comment_delete.html'

    def get_success_url(self):
        comment = get_object_or_404(Comment,pk=self.kwargs['pk'])
        return redirect('book_summary:book_detail',pk=comment.book.pk)


class BigCategoryView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        bigcategory = get_object_or_404(BigCategory,pk=self.kwargs['pk'])
        queryset = Book.objects.order_by('-published_date').filter(bigcategory=bigcategory)
        return queryset


class CategoryView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category,pk=self.kwargs['pk'])
        queryset = Book.objects.order_by('-published_date').filter(category=category)
        return queryset


class PublisherView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        publisher = get_object_or_404(Publisher,pk=self.kwargs['pk'])
        queryset = Book.objects.order_by('-published_date').filter(publisher=publisher)
        return queryset


class AuthorView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        author = get_object_or_404(Author,pk=self.kwargs['pk'])
        queryset = Book.objects.order_by('-published_date').filter(author=author)
        return queryset

class GoodBookView(generic.DetailView):
    model = Good
    template_name = 'book_summary/good_book'