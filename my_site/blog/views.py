from django.shortcuts import render, get_object_or_404

from .models import Post


all_posts = Post.objects.all()

# Create your views here.


def starting_page(request):
    # Get the first 3 latest post in descending order by date
    latest_posts = all_posts.order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
