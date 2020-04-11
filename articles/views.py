from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article(request, slug):
    print(f'[slug] => {slug}')
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article.html', {'article': article})
