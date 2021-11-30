from django.shortcuts import render
from django.views.generic import ListView

from articles.models import Article, Scope, Tag


DATA = ['Культура', 'Город', 'Здоровье', 'Наука', 'Космос', 'Международные отношения']


def add_data():
    tags = Tag.objects.all()
    if len(tags) == 0:
        for name_tag in DATA:
            Tag.objects.create(name=name_tag)


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/news.html'

    def get_context_data(self, **kwargs):
        add_data()
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.all()
        return context
