from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from taggit.models import Tag
from .models import Post, Comment, Contact
from .forms import EmailPostForm, CommentForm, SearchForm, ContactForm
from django.db.models import Q
# Create your views here.


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag         = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator   = Paginator(object_list, 6)
    page        = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    all_tags = Post.tags.all()
    context = {
        'posts'    : posts,
        'page'     : page,
        'tag'      : tag,
        'all_tags' : all_tags,
    }
    return render(request, "list.html", context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,  slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    post_tag_ids  = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    post.views += 1
    post.save()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            context = {
                'post'         : post,
                'comment_form' : comment_form,
                'similar_posts': similar_posts,
            }
            return render(request, "detail.html", context)
    else:
        comment_form = CommentForm()
    context = {
        'post'         : post,
        'comment_form' : comment_form,
        'similar_posts': similar_posts,
    }
    return render(request, "detail.html", context)

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(d['name'],d['email'],post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, d['name'], d['comments'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [d['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post' : post,
        'form' : form,
        'sent' : sent,
    }
    return render(request, 'share.html', context)

def post_search(request):
    if 'query' in request.GET:
        query = request.GET.get('query')
        if query:
            queryset = Q(title__icontains=query) | Q(body__icontains=query)
            result = Post.objects.filter(queryset).distinct()
    context = {
        'result': result,
        'query' : query
    }
    return render(request, 'search.html', context)

def contact(request):
    msg = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        model = Contact()
        if form.is_valid():
            msg           = True
            model.name    = form.cleaned_data['name']
            model.email   = form.cleaned_data['email']
            model.subject = form.cleaned_data['subject']
            model.message = form.cleaned_data['message']
            model.save()
    else:
        form = ContactForm()
    context = {
        'form' : form,
        'msg'  : msg,
    }
    return render(request, "contact.html", context)
