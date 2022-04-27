from django.shortcuts import render, redirect
from .models import Comment, Authorizing
from .models import Course
from .models import News
from .forms import CommentForm, AuthorizeForm
from django.views.generic import UpdateView, DeleteView, DetailView

# Create your views here.
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details.html'
    context_object_name = 'news'

def news_home(request):
    new = News.objects.all()
    return render(request, 'news/news_home.html', {'new': new})

def create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            try:
                form.save()
                return redirect('create')
            except:
                form.add_error(None, 'Oшибка')

    else:
        form = CommentForm()


    return render(request, 'news/create.html', {'form': form})

def authorize(request):
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)

        if form.is_valid():

            try:
                #form.save()
                Authorizing.objects.create(**form.cleaned_data)

                return redirect('authorize')
            except:
                form.add_error(None, 'Oшибка')

    else:
        form = AuthorizeForm()


    return render(request, 'news/authorize.html', {'form': form})

class NewUpdateView(UpdateView):
    model = Comment
    template_name = 'news/create.html'
    form_class = CommentForm

class NewDeleteView(DeleteView):
    model = Comment
    success_url = '/news/comments'
    template_name = 'news/news-delete.html'

def comments(request):
    com = Comment.objects.all()
    return  render(request, 'news/comments.html', {'com': com})


def courses(request):
    cours = Course.objects.all()
    return render(request, 'news/courses.html', {'cours': cours})