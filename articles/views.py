from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article(request, slug):
    print(f'[slug] => {slug}')
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article.html', {'article': article})


@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        # validating fields
        form = forms.CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            article_instance = form.save(commit=False)
            article_instance.author = request.user
            article_instance.save()
            return redirect('articles:article_list')
    else:
        form = forms.CreateArticleForm()
    return render(request, 'articles/article_new.html', {'form': form})
