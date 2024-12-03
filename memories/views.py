from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm, PostForm
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/home.html"
    
class PostLists(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/memories.html"
    paginate_by = 6

class AboutView(TemplateView):
    template_name = 'memories/about.html'
    
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'memories/create_post.html'
    # fields = ('title', 'theme', 'excerpt', 'content', 'post_image')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.instance.status = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])
class PendingPostView(TemplateView):
    template_name = 'memories/post_pending.html'
    
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'memories/edit_post.html'
    fields = ('theme', 'excerpt', 'content', 'post_image')
    def form_valid(self, form):
        # Ensure no changes to slug or author
        form.instance.slug = self.object.slug
        form.instance.author = self.object.author
        return super().form_valid(form)
    def test_func(self):
        # Ensure the current user is the author
        post = self.get_object()
        return self.request.user == post.author
    def handle_no_permission(self):
        # Redirect unauthorized users to the home page with a message
        messages.error(self.request, "You do not have permission to edit this post.")
        return redirect('home')
    def get_success_url(self):
        # Redirect to the post detail page after successful edit
        return reverse('post_detail', args=[self.object.slug])
    

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

