from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
from django.views.generic import TemplateView

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/index.html"
    
class PostLists(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/memories.html"
    paginate_by = 6

class AboutView(TemplateView):
    template_name = 'memories/about.html'

def post_detail(request, slug):
    """
    Display an individual :model:`memories.Post`.

    **Context**

    ``post``
        An instance of :model:`memories.Post`.

    **Template:**

    :template:`memories/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,'Comment submitted and awaiting approval'
    )
        
    comment_form = CommentForm()


    return render(
        request,
        "memories/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }
    )