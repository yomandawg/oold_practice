from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article, Comment
from IPython import embed

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-id')
    # embed()
    context = {
        'articles': articles,
    }
    return render(request, 'board/list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'board/detail.html', context)

# def new_article(request):
#     return render(request, 'board/new.html')

def create_article(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)
    elif request.method == 'GET':
        return render(request, 'board/new.html')

# TODO: update action
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        context = {
            'article': article
        }
        return render(request, 'board/edit.html', context)
    elif request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail', article.id)

def delete_article(request, article_id):
    # embed()
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('board:article_list')
    elif request.method == 'GET':
        return redirect('board:article_detail', article.id)

# model comment
def create_comment(request, article_id):
    # /board/10000/comments/create => False value
    article = get_object_or_404(Article, id=article_id) # defense mechanism
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        # comment.article_id = article.id # foreign key 설정하면 자동으로 article_id 생김
        comment.article = article # 객체 자체를 넣어도 ORM이 자동으로 article_id 배정해줌
        comment.save()
    return redirect('board:article_detail', article.id)

def delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
    return redirect('board:article_detail', article.id)

