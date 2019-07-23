from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Blog.forms import BlogPostForm, CommentForm
from Blog.models import BlogPost


def paginated_results(request, results, split_number=10):
    # split number is the number of paginated items
    # this method allows pagination of Django Data Objects
    p = Paginator(results, split_number)
    page = request.GET.get('page', 1)
    search_results = p.get_page(page)

    # used like this in template context
    # 'posts': paginated_results(request, posts)

    return search_results


def view_posts(request):
    # this is the view used to view posts
    # these are the posts passed to the page
    posts = list(BlogPost.objects.all().order_by('submitted_at'))
    # this renders the html template
    return render(request, 'view.html', {
        'posts': posts
        # add more context data here if needed just as above...
    })


def create(request):
    # this is the form used to enter a blog post
    form = BlogPostForm(request.POST or None, request.FILES or None)
    # if the form is posted
    if request.method == 'POST':
        # checking to ensure the form is valid
        if form.is_valid():
            print('form valid')
            form.save()
            # form was saved so we are redirecting to the view page
            return redirect(reverse('post_view'))
        else:
            print(form.errors)
    # render the template
    return render(request, 'create.html', {
        'form': form
    })


def create_comment(request, id):
    # getting the post object from the URL param 'id'.
    # You can only create a comment for a post right?
    post = get_object_or_404(BlogPost, id=id)
    # this is the form to submit a comment
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        # checking if form is vaild on submission
        if form.is_valid():
            comment = form.save(commit=False)
            # setting the proper post variable
            comment.post = post
            comment.save()
            print('form valid')
            # all was saved so we redirect
            return redirect(reverse('post_view'))
    # render the template
    return render(request, 'create_comment.html', {
        'form': form
    })


def edit(request, id):
    # getting the post object from the URL param 'id'.
    post = get_object_or_404(BlogPost, id=id)
    # the form to edit the blog post
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            print('form valid')
            form.save()
            # form valid and object updated so redirect
            return redirect(reverse('post_view'))
    # render the template
    return render(request, 'edit.html', {
        'post': post,
        'form': form,
    })


def delete(request, id):
    # here we delete the post
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, id=id)
        post.delete()
        # the object was deleted successfully so we redirect
        return redirect(reverse('post_view'))
    else:
        # you should know why this is not safe
        raise Exception('Not a POST, deleting not safe')
