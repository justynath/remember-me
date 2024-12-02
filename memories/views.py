from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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
    
class AddPost(CreateView):
    model = Post
    template_name = 'memories/create_post.html'
    fields = ('title', 'theme', 'excerpt', 'content', 'post_image')

    def form_valid(self, form):
        # Set the author to the logged-in user
        form.instance.author = self.request.user

        # Automatically generate the slug from the title
        form.instance.slug = slugify(form.instance.title)

        # Ensure the status is set to 'Draft' (0)
        form.instance.status = 0

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to a confirmation page
        return reverse_lazy('post_pending')
    
class PendingPostView(TemplateView):
    template_name = 'memories/post_pending.html'

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

